/** Checks every pun fits its PunCard text box (src/lib/punFit.ts); reports any that need more
 * than PUN_MAX_LINES lines or fall back to the minimum size. Usage: node scripts/check_puns.mts */
import { existsSync, readFileSync } from "node:fs";
import { join } from "node:path";
import { fitPun, PUN_MAX_LINES, PUN_MIN_PX } from "../src/lib/punFit.ts";

const ROOT = new URL("..", import.meta.url).pathname.replace(/^\/([a-zA-Z]:)/, "$1");
let checked = 0;
const flagged: string[] = [];
const sizes = new Map<number, number>();
for (let ep = 1; ep <= 86; ep++) {
  const file = join(ROOT, "episodes", `ep${String(ep).padStart(3, "0")}.json`);
  if (!existsSync(file)) continue;
  const pun = (JSON.parse(readFileSync(file, "utf-8")) as { pun: string }).pun;
  const fit = fitPun(pun);
  checked++;
  sizes.set(fit.size, (sizes.get(fit.size) ?? 0) + 1);
  if (fit.lines > PUN_MAX_LINES || fit.size === PUN_MIN_PX) {
    flagged.push(`ep${ep}: ${fit.lines} lines at ${fit.size}px (${pun.length} chars)`);
  }
}
console.log(`puns checked: ${checked}`);
console.log(
  `sizes: ${[...sizes.entries()]
    .sort((a, b) => b[0] - a[0])
    .map(([s, n]) => `${s}px x${n}`)
    .join(", ")}`,
);
console.log(
  flagged.length
    ? `needs more than ${PUN_MAX_LINES} lines:\n${flagged.join("\n")}`
    : `all puns fit in ${PUN_MAX_LINES} lines or fewer`,
);
