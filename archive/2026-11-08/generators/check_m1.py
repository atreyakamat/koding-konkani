import json,re,subprocess,tempfile,os,gen
E={n:json.load(open(f"repo_py/episodes/ep{n:03d}.json")) for n in range(1,13)}
md=open("py_m01.md").read()
bad=[]
def fail(*a): bad.append(a); print("FAIL",*a)
for n in range(5,13):
    e=E[n]; sc=e["scenes"]
    for x in sc: x["template"]=x["template"].replace("-"," ").capitalize().replace("Bug of the day","Bug of the Day")
    # 1 timing
    t=0
    for s in sc:
        if s["startSec"]!=t: fail(n,"gap",s["id"])
        t+=s["lengthSec"]
    if t!=e["lengthSec"] or not 300<=t<=340: fail(n,"total",t)
    # 2 chapters
    yt=e["youtube"]; ch=yt["chapters"]
    starts={s["id"]:s["startSec"] for s in sc}
    st=sorted(starts.values())
    for c in ch:
        m,s_=c["t"].split(":"); sec=int(m)*60+int(s_)
        if sec not in st: fail(n,"chapter not at scene start",c)
    if ch[0]["t"]!="0:00": fail(n,"first chapter")
    # 3 HL / TRACK
    code=[s for s in sc if s.get("code")]
    for s in sc:
        hls=[int(x) for x in re.findall(r"\[HL (\d+)\]",s["narration"])]
        if s["template"]!="Code explain" and hls: fail(n,"HL in non-code",s["id"])
        if s["template"]=="Code explain":
            if not s.get("code"): fail(n,"CE no code",s["id"])
            else:
                nl=len(s["code"]["source"].splitlines())
                if any(h<1 or h>nl for h in hls): fail(n,"HL range",s["id"],hls,nl)
                if not hls: fail(n,"CE without HL",s["id"])
        for nm in re.findall(r"\[TRACK (\w+)=",s["narration"]):
            src=(s.get("code") or code[0]["code"])["source"]
            if not re.search(r"\b"+nm+r"\b",src): fail(n,"TRACK name",nm)
    # 4 pace
    for s in sc:
        w=gen.words(s["narration"])
        if s["template"]!="Pun card" and w/s["lengthSec"]>1.85: fail(n,"pace",s["id"],w/s["lengthSec"])
    if len(e["shorts"])!=5: fail(n,"shorts")
    for sh in e["shorts"]:
        if len(sh["hook"].split())>9: fail(n,"hook",sh["id"])
        if any(f<1 or f>11 for f in sh["fromScenes"]): fail(n,"fromScenes",sh)
        if gen.words(sh["script"])/sh["lengthSec"]>2.0: fail(n,"short pace",sh["id"])
    # 6 style
    txt=json.dumps(e,ensure_ascii=False)
    if re.search(r"[\U0001F300-\U0001FAFF☀-➿]",txt): fail(n,"emoji")
    outro=sc[-1]["narration"]
    if not outro.rstrip().endswith("Keep coding, says Xecxec!"): fail(n,"signoff")
    if sc[-1]["template"]!="Outro" or sc[7]["template"]!="Bug of the Day" or sc[8]["template"]!="Pun card" or sc[6]["name"]!="Recap" if "name" in sc[6] else False: fail(n,"order")
    tpl=[s["template"] for s in sc]
    exp=["Title card","Concept slide","Code explain",None,"Code explain","Terminal","Concept slide","Bug of the Day","Pun card","Challenge","Outro"]
    for i,(a,b) in enumerate(zip(tpl,exp)):
        if b and a!=b: fail(n,"tpl",i+1,a,b)
    if tpl[3] not in("Concept slide","Memory boxes"): fail(n,"tpl4")
    # 7 real run
    for cf in e["codeFiles"]:
        ok,err,out=gen.run_py(cf["file"],cf["source"],(cf.get("stdin") or "")+"\n" if cf.get("stdin") else None)
        if not ok or out.strip()!=cf["output"].strip(): fail(n,"output mismatch",cf["file"],out,cf["output"])
    b=e["bug"]
    ok,err,out=gen.run_py("x.py",b["wrong"],"4\n" if n==8 else None)
    if ok: fail(n,"bug does not fail")
    else:
        last=err.splitlines()[-1]
        if last not in b["error"]: fail(n,"bug error text",last)
    ok,err,out=gen.run_py("x.py",b["fixed"],"4\n" if n==8 else None)
    if not ok: fail(n,"fixed fails",err)
    if len(b["error"].splitlines())>8: fail(n,"err >8 lines")
    if "/tmp" in b["error"] or "\\" in b["error"]: fail(n,"path leak")
# 5 distinct across M0+M1
puns=[E[n]["pun"] for n in E]; bugs=[E[n]["bug"]["error"].splitlines()[-1] for n in E]
if len(set(puns))!=len(puns): fail("dup puns")
if len(set(bugs))!=len(bugs): fail("dup bug lines",bugs)
if len({E[n]["challenge"] for n in E})!=len(E): fail("dup challenge")
print("FAILS:",len(bad))
