# Module 10 — Dynamic memory

Episodes 65–68 · Mint + Tomato

## EP 65 — Stack vs Heap

**Module 10 · Dynamic memory · 6:45 · Mint + Tomato · Prerequisite: EP 57, EP 59**

**Learning goals:** name the three places a C variable can live (stack, heap, global area) and say how long each lasts; explain why a huge local array crashes the program; ask for one heap `int` with `malloc` and give it back with `free`.

### YouTube

- **Title:** Stack vs Heap Explained With a Godown | C Programming EP 65
- **Description:** Your local variables live in a small, tidy room called the stack. When you need more space, or memory that outlives a function, you rent a godown called the heap. We draw both, print real addresses from each, and crash the stack on purpose. 0:00 Your room vs a godown · 0:20 Title · 0:25 The stack, frame by frame · 1:30 The heap · 2:20 Code, line by line · 3:45 Running it · 4:10 Pun · 4:15 Stack vs heap at a glance · 4:55 Bug of the Day: huge array on the stack · 6:00 Challenge · 6:25 Next episode
- **Tags:** stack vs heap in c, dynamic memory allocation c, malloc in c, stack overflow c, heap memory, memory layout c program, local variables stack, c programming tutorial, learn c, koding konkani, c programming india, engineering c
- **Thumbnail:** big text "STACK vs HEAP"; left: a small tidy room with stacked plates labelled `main`, `visit`; right: a big godown with crates; a black arrow from a stack box `godown` to a heap crate; Xecxec carrying a crate, sweating; mint background, tomato text block

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:20 | Concept slide | Xecxec's small bedroom with a shelf; a large rented godown near Margao market with a padlock and a rent receipt | Xecxec stuffs boxes on the shelf until it overflows; cuts to him unlocking the godown; door creak |
| 2 | 0:20 | 0:05 | Title card | EP 65 · STACK VS HEAP | Title slams in on mint; claw-click |
| 3 | 0:25 | 1:05 | Memory boxes | Tall column labelled STACK: frame `main` (room) at the bottom, frame `visit` (local) stacked on it | Frames stack like plates with a clink; `visit` frame lifts off and disappears when the function returns; whoosh |
| 4 | 1:30 | 0:50 | Memory boxes | Second region labelled HEAP, far from the stack; one crate holding 500; stack box `godown` with an arrow to it; small GLOBAL region with `global_count` | Crate drops into the heap with a thud; arrow draws from `godown`; padlock icon on the crate until `free` |
| 5 | 2:20 | 1:25 | Code explain | `places.c` (26 lines); tracker: room, local, godown, \*godown | Butter highlights; corner map of the three regions lights up the right region per line |
| 6 | 3:45 | 0:25 | Terminal | Compile and run; sticky note "your addresses will differ" | Output prints; each line gets a coloured tag: stack (lilac), global (butter), heap (mint) |
| 7 | 4:10 | 0:05 | Pun card | "Why did the variable move to the heap? The stack was too crowded." | Card flips; Xecxec waves a rent receipt; rimshot |
| 8 | 4:15 | 0:40 | Concept slide | Comparison table: size, speed, who frees it, lifetime | Rows slide in one by one; mint ticks and tomato crosses |
| 9 | 4:55 | 1:05 | Bug of the Day | `int big[10000000];` inside `main`; crash; then the `malloc` fix | Stack column fills from the bottom and bursts through the top; crash crunch; fixed version moves the block to the heap with a crate drop |
| 10 | 6:00 | 0:25 | Challenge | "Explain stack vs heap in 3 lines" task card | Three blank lines fill with a typing sound; Xecxec taps |
| 11 | 6:25 | 0:20 | Outro | "Next: EP 66 · malloc & free — borrow memory, return it" | A crate handed over and handed back; sign-off |

### Narration script

**\[1 · Your room vs a godown\]** Your room has one small shelf. It's close, it's fast, and when you move out, it's cleared automatically. But try to keep fifty sacks of rice on it, and it collapses. For big things, you rent a godown. It's huge, you get the key, and it stays yours until you hand the key back. Your C program has both: a room called the stack, and a godown called the heap.

**\[2 · Title\]** Episode sixty-five. Stack versus heap. Welcome to Module 10: dynamic memory.

**\[3 · The stack, frame by frame\]** You have already seen the stack, in EP 55 and EP 57. Every time a function is called, it gets a stack frame: a box for its local variables. When main starts, its frame goes on the stack, holding room. When main calls visit, visit's frame goes on top, holding local. Like plates stacked on a plate rack. When visit returns, its plate is removed, and local is gone. That's why, in EP 57, returning the address of a local array failed. The stack is very fast, and it cleans itself up. But it is small. On Windows, it's usually just 1 megabyte for the whole program. On Linux, it's usually 8.

**\[4 · The heap\]** The heap is a separate, much bigger area of memory. Memory on the heap does not belong to any function. It stays until you give it back. To rent a piece, you call malloc, which means "memory allocate". You tell it how many bytes you want. malloc finds space in the heap and returns its address. So we store that address in a pointer: here, godown, a stack variable that points to a crate in the heap. Everything you learned in Module 8 now pays off: the heap is only reachable through pointers. When you're done, you call free with that address, and the crate goes back. There's also a third, small area for global variables, which live for the whole program, like global\_count. So three places: stack for locals, heap for what you malloc, and the global area.

**\[5 · Code, line by line\]** Here is the program. \[HL 2\] Line 2 includes stdlib dot h. That's where malloc and free live. Forget it, and you'll get warnings. \[HL 4\] Line 4 creates a global variable, global\_count, outside every function. \[HL 6\] Lines 6 to 9 define visit. \[HL 7\] Line 7 makes a local int inside visit. \[TRACK local=5\] \[HL 8\] Line 8 prints its address. \[HL 12\] Now main. Line 12 makes room, a local in main's frame. \[TRACK room=1\] \[HL 13\] Line 13 is new: int star godown equals malloc of sizeof int. sizeof int is 4 on our computers, so we ask for 4 bytes. malloc returns the address of those bytes on the heap, and godown stores it. \[TRACK godown=heap\] \[HL 14\] Line 14 checks if godown is NULL. Remember EP 59: malloc returns NULL if it cannot find enough memory. \[HL 15\] If so, line 15 returns 1 to signal an error. \[HL 17\] Line 17 writes 500 through the pointer, into the heap crate. \[TRACK \*godown=500\] \[HL 19\] Lines 19 to 22 print four addresses: room, visit's local, the global, and the heap crate. \[HL 24\] Line 24: free of godown. We hand the key back. \[HL 25\] Return zero.

**\[6 · Running it\]** Compile and run. Look at the addresses. room and local are close together. They're both on the stack, and local is a little lower, because on most PCs the stack grows downward. The global and the heap crate are in completely different areas. Your exact numbers will differ, and on Windows they look different from Linux, but you'll still see the stack addresses grouped together and the heap somewhere else.

**\[7 · Pun\]** Why did the variable move to the heap? The stack was too crowded.

**\[8 · Stack vs heap at a glance\]** Let's compare. Size: the stack is small, about 1 megabyte on Windows; the heap can use most of your RAM. Speed: the stack is faster, but the heap is still fast enough for almost everything. Cleaning up: the stack cleans itself when a function returns; the heap is your job, with free. Lifetime: stack memory dies with its function; heap memory lives until you free it. Rule of thumb: small and short-lived, use the stack. Big, or needs to outlive the function, or size known only while running, use the heap.

**\[9 · Bug of the Day\]** Today's bug: a huge array on the stack. int big square bracket ten million, inside main. Ten million ints is 40 megabytes. The stack on Windows is 1 megabyte. GCC compiles it without a warning. But when you run it, the stack overflows. This is the real "stack overflow". On Linux you see segmentation fault. On Windows the program just closes, without printing anything. The fix: put big data on the heap. int star big equals malloc of ten million times sizeof int. Check for NULL. Use it like an array, with big square bracket 0, because from EP 57 you know a square bracket i is just star of big plus i. And free it at the end.

**\[10 · Challenge\]** Your challenge is in words, not code. In the comments, explain stack versus heap in three lines: where locals go, where malloc memory goes, and who cleans up each one. Bonus: say which one you would use for an array of one lakh ints, and why.

**\[11 · Outro\]** Now you know where memory lives. Next episode, we master malloc and free properly, and allocate exactly as much memory as the user asks for. Keep coding, says Xecxec!

### Code shown

```c
#include <stdio.h>
#include <stdlib.h>

int global_count = 0;

void visit(void) {
    int local = 5;
    printf("local in visit() at   %p (stack)\n", (void *)&local);
}

int main(void) {
    int room = 1;
    int *godown = malloc(sizeof(int));
    if (godown == NULL) {
        return 1;
    }
    *godown = 500;

    printf("room in main() at     %p (stack)\n", (void *)&room);
    visit();
    printf("global_count at       %p (global)\n", (void *)&global_count);
    printf("heap int at           %p (heap), value %d\n", (void *)godown, *godown);

    free(godown);
    return 0;
}
```

**Expected output** (Linux sample; your addresses will differ, and on Windows they are printed as 16 hex digits without `0x`):

```text
room in main() at     0x7ffcd9774c2c (stack)
local in visit() at   0x7ffcd9774c04 (stack)
global_count at       0x56265c7e2014 (global)
heap int at           0x56265e58e2a0 (heap), value 500
```

### Bug of the Day

```c
#include <stdio.h>

int main(void) {
    int big[10000000];
    big[0] = 1;
    printf("%d\n", big[0]);
    return 0;
}
```

`gcc -Wall bug.c` gives **no warning**. Running it overflows the stack (40 MB array, 1 MB default stack on Windows, 8 MB on Linux): `Segmentation fault` on Linux; on Windows the program exits without printing anything.

Fixed:

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int *big = malloc(10000000 * sizeof(int));
    if (big == NULL) {
        printf("Not enough memory\n");
        return 1;
    }
    big[0] = 1;
    printf("%d\n", big[0]);
    free(big);
    return 0;
}
```

```text
1
```

Why: local arrays live on the small stack; large data belongs on the heap, which can hold far more.

### Pun & challenge

- **Pun:** "Why did the variable move to the heap? The stack was too crowded."
- **Challenge:** In three lines, explain stack vs heap: where locals go, where `malloc` memory goes, and who cleans up each. Bonus: where would you put an array of 1,00,000 ints, and why?
- **Challenge answer:** Locals live on the stack and vanish automatically when their function returns. `malloc` memory lives on the heap and stays until you call `free`. The stack is small (about 1 MB on Windows), so 1,00,000 ints (400 KB) is risky there; use the heap with `malloc` and `free`.

### Shorts for EP 65

**S1 · Your room vs a godown** — 0:25 · built from scenes 1, 3 and 4

- **Hook (first 1.5s):** A shelf collapses under rice sacks: "This is a stack overflow."
- **Script:** Your C program has two places for data. The stack is your room: small, fast, and cleaned automatically when a function ends. The heap is a rented godown: big, and yours until you hand back the key. Locals go on the stack. malloc gives you heap memory.
- **On-screen text:** STACK = ROOM · HEAP = GODOWN
- **Caption + hashtags:** The easiest way to remember it. #cprogramming #memory #kodingkonkani #learntocode #ctutorial

**S2 · Stack vs heap in 30 seconds** — 0:30 · built from scene 8

- **Hook (first 1.5s):** Two columns slam in: STACK and HEAP.
- **Script:** Stack: small, about one megabyte on Windows, very fast, cleaned automatically, dies with the function. Heap: big, slightly slower, you clean it with free, lives until you free it. Small and short-lived? Stack. Big, or needs to outlive the function? Heap.
- **On-screen text:** SMALL → STACK · BIG → HEAP
- **Caption + hashtags:** Screenshot this for your exam. #cprogramming #memory #kodingkonkani #codingtips #stackvsheap

**S3 · The real stack overflow** — 0:30 · built from scene 9

- **Hook (first 1.5s):** A stack column bursting through its top.
- **Script:** int big of ten million, inside main. 40 megabytes. The Windows stack is 1 megabyte. No warning from GCC, but the program dies instantly. That's a real stack overflow. Fix: malloc it on the heap, check for NULL, and free it at the end.
- **On-screen text:** 40 MB DOES NOT FIT IN 1 MB
- **Caption + hashtags:** Now you know where the website got its name. #cprogramming #debugging #kodingkonkani #stackoverflow #cbugs

**S4 · Too crowded** — 0:12 · built from scene 7

- **Hook (first 1.5s):** Xecxec squeezed between plates on a plate rack.
- **Script:** Why did the variable move to the heap? The stack was too crowded.
- **On-screen text:** THE STACK WAS TOO CROWDED
- **Caption + hashtags:** Moving day for variables. #programmerhumor #cprogramming #kodingkonkani #codingmemes #memory

**S5 · Quiz: stack or heap?** — 0:25 · built from scenes 8 and 10

- **Hook (first 1.5s):** "1,00,000 ints. Stack or heap?"
- **Script:** Quick quiz. An int counter in a loop: stack or heap? Stack. An array of one lakh ints that a function must return: stack or heap? Heap, because it's big and must outlive the function. Explain stack versus heap in three lines in the comments.
- **On-screen text:** STACK OR HEAP?
- **Caption + hashtags:** Comment your three lines. #cprogramming #codingquiz #kodingkonkani #memory #learntocode

## EP 66 — malloc & free

**Module 10 · Dynamic memory · 7:00 · Mint + Tomato · Prerequisite: EP 65**

**Learning goals:** allocate an array whose size is chosen at run time with `malloc(n * sizeof(int))`; always check the result for `NULL`; use the memory like a normal array; release it with `free` and then set the pointer to `NULL`.

### YouTube

- **Title:** malloc and free: Borrow Memory, Return It | C EP 66
- **Description:** How many students are in the class? You only find out when the program runs. With malloc you ask for exactly that much memory, use it like an array, and give it back with free. We draw every byte, then watch a program leak memory until it runs dry. 0:00 The shamiana hire shop · 0:20 Title · 0:25 Asking for bytes · 1:25 Check, use, free · 2:15 Code, line by line · 4:05 Running it · 4:30 Pun · 4:35 The four-step habit · 5:05 Bug of the Day: forgetting free · 6:15 Challenge · 6:40 Next episode
- **Tags:** malloc in c, free in c, dynamic memory allocation, malloc sizeof, memory leak c, null check malloc, dynamic array c, c programming tutorial, learn c, koding konkani, c programming for beginners, c programming india
- **Thumbnail:** big text "BORROW. RETURN."; a mint heap with a row of crates labelled `marks[0..2]`, a black arrow from `marks`; a tomato "free()" stamp; Xecxec handing back a key; mint background, tomato text block

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:20 | Concept slide | A Goan wedding shamiana hire shop: "How many chairs?" sign; Xecxec writes "3"; three chairs are carried out; later returned | Chairs carried out one by one; ledger tick; chairs returned; till-bell |
| 2 | 0:20 | 0:05 | Title card | EP 66 · MALLOC & FREE | Title slams in; claw-click |
| 3 | 0:25 | 1:00 | Memory boxes | Stack: `n` = 3, `marks` (pointer). Heap: a 12-byte block at 0x5000 split into three 4-byte boxes; label "n \* sizeof(int) = 3 \* 4 = 12 bytes" | Formula types out; block drops into the heap; arrow draws from `marks` to the first box |
| 4 | 1:25 | 0:50 | Memory boxes | Same diagram; boxes fill with 60, 70, 80; then `free(marks)` greys the block; then `marks = NULL` turns the arrow into a NULL sign | Values pop in; grey wash on free with a key-return clink; arrow snaps off into a NULL sign |
| 5 | 2:15 | 1:50 | Code explain | `marks.c` (29 lines); tracker: n, marks, i, marks\[i\] | Butter highlights; corner heap diagram mirrors scenes 3–4 |
| 6 | 4:05 | 0:25 | Terminal | Two runs: input 3, then input -5 | First run prints three students; second prints the error line; tomato flash |
| 7 | 4:30 | 0:05 | Pun card | "malloc and free are best friends. One lends, the other always pays back." | Card flips; Xecxec shakes his own claw; rimshot |
| 8 | 4:35 | 0:30 | Concept slide | Four-step habit: 1 malloc with sizeof, 2 check NULL, 3 use, 4 free and set NULL | Steps tick one by one in mint |
| 9 | 5:05 | 1:10 | Bug of the Day | `make_order()` that mallocs 4,000 bytes and never frees, called 1,00,000 times; heap filling with grey abandoned crates | Crates pile up and nobody points at them; a memory meter climbs to about 400 MB; alarm; fixed version adds `free(order);` and the meter stays flat |
| 10 | 6:15 | 0:25 | Challenge | "Allocate n marks, read them, print the average" task card | Input boxes fill; average pops |
| 11 | 6:40 | 0:20 | Outro | "Next: EP 67 · calloc & realloc — need a bigger basket" | A fish basket grows bigger; sign-off |

### Narration script

**\[1 · The shamiana hire shop\]** When your family plans a wedding in Goa, you go to the hire shop for chairs. The shopkeeper asks: how many? You say three hundred. He gives you exactly three hundred, and writes it in his ledger. After the wedding, you return them all. malloc is the hire shop. free is returning the chairs.

**\[2 · Title\]** Episode sixty-six. malloc and free.

**\[3 · Asking for bytes\]** Last episode, we used malloc for one int. Today, a whole array, with a size we only learn while the program is running. Say the user types 3 students. malloc does not understand "3 ints". It only understands bytes. So we calculate: n times sizeof int. 3 times 4 is 12 bytes. malloc finds 12 free bytes in the heap, say at 0x5000, and returns that address. We store it in a pointer called marks. Now look closely: the heap block is three int boxes in a row, and marks points to the first one. That's exactly what an array looks like from EP 57. So we can write marks square bracket i, just like a normal array.

**\[4 · Check, use, free\]** Now we fill the boxes: 60, 70, 80. When we're done, we call free of marks. The block goes back to the heap. It's greyed out. But look at marks. It still holds 0x5000! free does not change your pointer. The arrow still points at memory you've returned. That's a trap, and we'll study it in EP 68. So after free, we set marks to NULL. Now the arrow is gone, and nobody can use it by mistake.

**\[5 · Code, line by line\]** Here's the program. \[HL 2\] Line 2 includes stdlib dot h for malloc and free. \[HL 5\] Line 5 creates n. \[HL 6\] Line 6 asks how many students. \[HL 7\] Line 7 reads n with scanf. scanf returns how many values it read. If it's not 1, or if n is zero or negative, \[HL 8\] line 8 prints an error, \[HL 9\] and line 9 returns 1. Never pass a negative size to malloc. \[TRACK n=3\] \[HL 12\] Line 12 is the key line: int star marks equals malloc of n times sizeof int. We ask for 12 bytes and get the address of the first. \[TRACK marks=0x5000\] \[HL 13\] Line 13: if marks is NULL, malloc failed. \[HL 14\] Line 14 prints a message, \[HL 15\] and line 15 returns 1. Always check. \[HL 18\] Lines 18 to 20 fill the array. For our demo, each student gets 60 plus i times 10. \[TRACK marks\[0\]=60\] \[TRACK marks\[1\]=70\] \[TRACK marks\[2\]=80\] \[HL 22\] Lines 22 to 24 print each student's marks, numbered from 1. \[HL 26\] Line 26: free of marks. Chairs returned. \[HL 27\] Line 27: marks equals NULL. Arrow removed. \[TRACK marks=NULL\] \[HL 28\] Line 28: return zero.

**\[6 · Running it\]** Compile and run. Type 3. Student 1: 60, student 2: 70, student 3: 80. Run it again and type 5, and you get five students. Same program, different amount of memory. That's the power of dynamic memory. Now try minus 5. The program politely refuses.

**\[7 · Pun\]** malloc and free are best friends. One lends, the other always pays back.

**\[8 · The four-step habit\]** Every time you use malloc, do these four steps. One: malloc with sizeof, never a guessed number. Two: check for NULL. Three: use the memory. Four: free it, and set the pointer to NULL. Make it a habit, like locking your scooter.

**\[9 · Bug of the Day\]** Today's bug: forgetting free. Here, a function make\_order mallocs 1000 ints, 4000 bytes, and uses it. But it never calls free. When the function returns, its local pointer order disappears from the stack. The heap block is still there, but nobody has its address any more. Nobody can ever free it. That is a memory leak. Now main calls make\_order one lakh times. One lakh times 4000 bytes is about 400 megabytes of lost memory. GCC gives no warning, and the program still prints "Done". But open Task Manager while it runs, and you'll see its memory climb. In a program that runs for days, like a server or a game, leaks eventually eat all the RAM. The fix is one line: free of order, before the function ends. On Linux, a tool called Valgrind can find leaks for you, and it reports them as "definitely lost".

**\[10 · Challenge\]** Your challenge. Ask the user how many marks they have. malloc exactly that many ints. Read each mark with scanf, add them up, and print the average with two decimal places. Then free the memory. With marks 70, 80 and 95, you should get 81.67. Pause and try.

**\[11 · Outro\]** You can now borrow exactly the memory you need, and return it. But what if you need more space later? Next episode: calloc and realloc. Keep coding, says Xecxec!

### Code shown

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n;
    printf("How many students? ");
    if (scanf("%d", &n) != 1 || n <= 0) {
        printf("Please enter a positive number.\n");
        return 1;
    }

    int *marks = malloc(n * sizeof(int));
    if (marks == NULL) {
        printf("Could not get memory.\n");
        return 1;
    }

    for (int i = 0; i < n; i++) {
        marks[i] = 60 + i * 10;
    }

    for (int i = 0; i < n; i++) {
        printf("Student %d: %d\n", i + 1, marks[i]);
    }

    free(marks);
    marks = NULL;
    return 0;
}
```

**Expected output** (user types `3`):

```text
How many students? 3
Student 1: 60
Student 2: 70
Student 3: 80
```

(user types `-5`):

```text
How many students? -5
Please enter a positive number.
```

### Bug of the Day

```c
#include <stdio.h>
#include <stdlib.h>

void make_order(void) {
    int *order = malloc(1000 * sizeof(int));
    if (order == NULL) return;
    order[0] = 1;
}

int main(void) {
    for (int i = 0; i < 100000; i++) {
        make_order();
    }
    printf("Done\n");
    return 0;
}
```

`gcc -Wall bug.c` gives **no warning**, and the program prints:

```text
Done
```

But it leaks 1,00,000 × 4,000 bytes (about 400 MB) while running; Task Manager shows its memory climbing. On Linux, Valgrind reports the leak (shown here for a 10-call version):

```text
==3504== 40,000 bytes in 10 blocks are definitely lost in loss record 1 of 1
==3504==    at 0x4846828: malloc (in /usr/libexec/valgrind/vgpreload_memcheck-amd64-linux.so)
==3504==    by 0x10917E: make_order (leak10.c:5)
==3504==    by 0x1091B2: main (leak10.c:12)
```

Fixed:

```c
void make_order(void) {
    int *order = malloc(1000 * sizeof(int));
    if (order == NULL) return;
    order[0] = 1;
    free(order);
}
```

Why: when the only pointer to a heap block disappears without `free`, that memory can never be returned.

### Pun & challenge

- **Pun:** "malloc and free are best friends. One lends, the other always pays back."
- **Challenge:** Ask for `n`, `malloc` `n` ints, read each mark, print the average to 2 decimals, then `free`.
- **Challenge answer:**

```c
int n;
printf("How many marks? ");
if (scanf("%d", &n) != 1 || n <= 0) return 1;

int *marks = malloc(n * sizeof(int));
if (marks == NULL) return 1;

int total = 0;
for (int i = 0; i < n; i++) {
    printf("Mark %d: ", i + 1);
    scanf("%d", &marks[i]);
    total += marks[i];
}
printf("Average: %.2f\n", (double)total / n);   /* 70 80 95 gives 81.67 */

free(marks);
```

### Shorts for EP 66

**S1 · Arrays of any size** — 0:25 · built from scenes 1 and 3

- **Hook (first 1.5s):** "How many students?" with a blinking cursor: "You don't know yet. That's fine."
- **Script:** A normal array needs its size when you write the code. But what if the user decides? malloc of n times sizeof int asks the heap for exactly that many bytes, and gives you the address. Use it like a normal array. Then free it. Like hiring chairs for a wedding.
- **On-screen text:** SIZE DECIDED AT RUN TIME
- **Caption + hashtags:** Exactly as much memory as you need. #cprogramming #malloc #kodingkonkani #learntocode #ctutorial

**S2 · The 4-step malloc habit** — 0:30 · built from scenes 4 and 8

- **Hook (first 1.5s):** Four mint ticks stamping one after another.
- **Script:** Four steps, every single time. One: malloc with sizeof. Two: check for NULL. Three: use the memory. Four: free it, and set the pointer to NULL. Why the last part? Because free returns the memory, but your pointer still points there.
- **On-screen text:** MALLOC · CHECK · USE · FREE
- **Caption + hashtags:** Make it muscle memory. #cprogramming #malloc #kodingkonkani #codingtips #memory

**S3 · The silent leak** — 0:35 · built from scene 9

- **Hook (first 1.5s):** Memory meter racing up to 400 MB.
- **Script:** This function mallocs 4000 bytes and forgets to free them. When it returns, the pointer is gone, but the memory is not. Call it one lakh times: about 400 megabytes lost. No warning, and the program still prints Done. One line fixes it: free.
- **On-screen text:** NO free = MEMORY LEAK
- **Caption + hashtags:** Silent, but deadly. #cprogramming #debugging #kodingkonkani #memoryleak #cbugs

**S4 · Best friends** — 0:12 · built from scene 7

- **Hook (first 1.5s):** Two crates labelled malloc and free high-fiving.
- **Script:** malloc and free are best friends. One lends, the other always pays back.
- **On-screen text:** ONE LENDS, ONE PAYS BACK
- **Caption + hashtags:** Friendship goals. #programmerhumor #cprogramming #kodingkonkani #codingmemes #malloc

**S5 · Quiz: how many bytes?** — 0:25 · built from scenes 3 and 10

- **Hook (first 1.5s):** `malloc(n * sizeof(int))` with n = 25.
- **Script:** Quick quiz. n is 25. How many bytes does malloc of n times sizeof int ask for, on a normal PC? Answer: 100, because an int is 4 bytes. Now the challenge: read n marks into malloc memory and print the average. Comment your code.
- **On-screen text:** n = 25 → ? BYTES
- **Caption + hashtags:** Did you say 100? #cprogramming #codingquiz #kodingkonkani #malloc #learntocode

## EP 67 — calloc & realloc

**Module 10 · Dynamic memory · 7:15 · Mint + Tomato · Prerequisite: EP 66**

**Learning goals:** use `calloc(count, size)` to get memory that starts as zeros, and say how it differs from `malloc`; grow a heap array with `realloc`; always store `realloc`'s result in a temporary pointer first; build a list that doubles its capacity when full.

### YouTube

- **Title:** Need a Bigger Basket? calloc and realloc | C EP 67
- **Description:** calloc gives you memory that is already cleaned to zero, and realloc lets a heap array grow while keeping what is inside. We fill a fish basket, watch it double in size, and see the one realloc mistake that throws away all your data. 0:00 The fish basket · 0:20 Title · 0:25 calloc: clean memory · 1:15 realloc: grow in place or move · 2:20 Code, line by line · 4:10 Running it · 4:30 Pun · 4:35 Why double the size? · 5:10 Bug of the Day: losing the pointer when realloc fails · 6:25 Challenge · 6:55 Next episode
- **Tags:** calloc in c, realloc in c, malloc vs calloc, dynamic array c, resize array c, realloc null, growing list c, dynamic memory allocation, learn c, koding konkani, c programming tutorial, c programming india
- **Thumbnail:** big text "BIGGER BASKET!"; a small mint basket of 2 fish next to a big one of 4 with arrows showing fish being moved across; Xecxec holding a fish in each claw; mint background, tomato text block

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:20 | Concept slide | Fisherwoman at Mapusa market with a 2-fish basket; more mackerels arrive; she swaps to a bigger basket and moves the fish across | Fish flop in; basket overflows; swap to bigger basket; splash SFX |
| 2 | 0:20 | 0:05 | Title card | EP 67 · CALLOC & REALLOC | Title slams in; claw-click |
| 3 | 0:25 | 0:50 | Memory boxes | Two heap blocks side by side: `malloc(3 * sizeof(int))` showing "? ? ?" and `calloc(3, sizeof(int))` showing "0 0 0" | malloc boxes flicker with random numbers; calloc boxes wipe clean to zero with a squeegee swipe |
| 4 | 1:15 | 1:05 | Memory boxes | Heap block of 2 ints (10, 20) at 0x5000 with pointer `basket`. Case A: free space after it, block stretches to 4 boxes in place. Case B: no space, a new 4-box block appears at 0x6000, 10 and 20 copied, old block greyed; `bigger` arrow then `basket` arrow move to 0x6000 | Case A: block stretches with a rubber sound. Case B: values fly across, old block greys out, arrow swings; whoosh |
| 5 | 2:20 | 1:50 | Code explain | `basket.c` (35 lines); tracker: capacity, count, basket, bigger | Butter highlights; corner heap diagram shows the basket growing 2 to 4 to 8 |
| 6 | 4:10 | 0:20 | Terminal | Compile and run | Output prints; "Basket grown" lines flash mint |
| 7 | 4:30 | 0:05 | Pun card | "realloc is like a Goan landlord: 'Need more space? Fine, but you might have to move house.'" | Card flips; Xecxec carries a suitcase; rimshot |
| 8 | 4:35 | 0:35 | Concept slide | Bar chart: growing by +1 needs 4 resizes for 5 fish, growing by doubling needs 2; at 1,000 items: 999 vs 9 | Bars rise; doubling bars stay short; tick SFX |
| 9 | 5:10 | 1:15 | Bug of the Day | `basket = realloc(basket, ...)` and realloc returns NULL; the 10 and 20 block is now unreachable | Arrow from `basket` snaps to NULL; old crate floats away, unreachable; sad trombone; fixed version with `bigger` slides in |
| 10 | 6:25 | 0:30 | Challenge | "Growing list: read numbers until -1" task card | Numbers drop into a basket that doubles twice |
| 11 | 6:55 | 0:20 | Outro | "Next: EP 68 · Memory bugs — the ghost pointer" | A faded ghost arrow floats over a greyed box; spooky whoo; sign-off |

### Narration script

**\[1 · The fish basket\]** At the Mapusa fish market, a fisherwoman starts the morning with a small basket for two fish. Then the boats come in, and she has more fish than space. So she gets a bigger basket and moves her fish across. She does not throw away the fish she already had. That's exactly what realloc does with memory.

**\[2 · Title\]** Episode sixty-seven. calloc and realloc.

**\[3 · calloc: clean memory\]** First, calloc. When malloc gives you memory, it's like a rented room that wasn't cleaned. Whatever the last program left there is still inside. So the boxes contain garbage until you fill them. calloc is different. It takes two arguments: how many items, and the size of each. calloc of 3 comma sizeof int. And it cleans the memory: every byte is set to zero. So all three ints start as 0. Use calloc when you want a fresh start, like counters or totals. Use malloc when you'll fill every box yourself straight away.

**\[4 · realloc: grow in place or move\]** Now realloc. Our basket holds 2 ints, 10 and 20, at address 0x5000. We need room for 4. We call realloc, passing the old pointer and the new size in bytes. One of two things happens. Case A: if there is free space right after our block, realloc simply stretches it. Same address. Case B: if there's no space, realloc finds a new, bigger block somewhere else, say at 0x6000, copies 10 and 20 across, and frees the old block for you. It returns the new address. So you must always use the address realloc returns, because the basket may have moved. And if realloc can't find any space at all, it returns NULL, and your old block is left untouched.

**\[5 · Code, line by line\]** Here's our fish basket program. \[HL 5\] Line 5: capacity is 2, the size of the basket; count is 0, how many fish are in it. \[TRACK capacity=2\] \[TRACK count=0\] \[HL 6\] Line 6: calloc of capacity comma sizeof int. Two ints, both zero. \[TRACK basket=0x5000\] \[HL 7\] Lines 7 to 9 check for NULL. \[HL 10\] Line 10 prints the two zeros from calloc. \[HL 12\] Line 12: a loop where fish goes 10, 20, 30, 40, 50. \[HL 13\] Line 13: is the basket full? count equals capacity? For 10 and 20, no. \[HL 24\] So we jump to line 24 and put the fish in basket square bracket count, \[HL 25\] then line 25 adds 1 to count. \[TRACK count=1\] \[TRACK count=2\] Now fish is 30, and count equals capacity. The basket is full. \[HL 14\] Line 14: new\_capacity is double: 4. \[HL 15\] Line 15, very important: int star bigger equals realloc of basket comma new\_capacity times sizeof int. We store the result in a new pointer called bigger, not in basket. You'll see why in the Bug of the Day. \[TRACK bigger=0x6000\] \[HL 16\] Line 16: if bigger is NULL, realloc failed. \[HL 17\] Line 17 frees the old basket, which is still valid, \[HL 18\] and line 18 returns 1. \[HL 20\] Line 20: success. Now we update basket to the new address. \[TRACK basket=0x6000\] \[HL 21\] Line 21 updates capacity to 4. \[TRACK capacity=4\] \[HL 22\] Line 22 prints "Basket grown to 4". Then 30 and 40 go in. At 50 the basket is full again, so it grows to 8. \[TRACK capacity=8\] \[HL 28\] Lines 28 to 31 print all the fish. \[HL 33\] Line 33 frees the basket. \[HL 34\] Return zero.

**\[6 · Running it\]** Compile and run. calloc gives 0 and 0. The basket grows to 4, then to 8. And all our fish are safe: 10, 20, 30, 40, 50. Nothing was lost when the basket moved.

**\[7 · Pun\]** realloc is like a Goan landlord. Need more space? Fine. But you might have to move house.

**\[8 · Why double the size?\]** Why do we double the capacity, and not just add one? Because each realloc may copy everything to a new place, which takes time. If you grow by one, you resize on almost every new item: for 1,000 items, that's 999 resizes. If you double, you only resize when you pass 2, 4, 8, 16 and so on: about 9 resizes for 1,000 items. Doubling is the standard trick used in real dynamic arrays.

**\[9 · Bug of the Day\]** Today's bug: losing your data when realloc fails. It's tempting to write basket equals realloc of basket comma new size. It compiles with no warning. And it works fine, until the day realloc fails. Then realloc returns NULL, and that NULL is stored straight into basket. Look at the diagram. The old block, with 10 and 20 inside, is still on the heap. But we just overwrote the only pointer to it. Our data is unreachable, and the block has leaked, because we can never free it. The fix is the pattern from our program: store realloc's answer in a temporary pointer like bigger. Check it. Only if it's not NULL, copy it into basket. If it is NULL, your old basket is still safe, and you can free it or keep using it.

**\[10 · Challenge\]** Your challenge: a growing list. Start with malloc for 4 ints. Read numbers from the user until they type minus 1. Whenever the list is full, double it with realloc, using the safe temporary-pointer pattern. At the end, print how many numbers were entered and all of them, then free. Try typing 5, 8, 13, 21, 34, 55, then minus 1. Pause and try.

**\[11 · Outro\]** Your arrays can now grow as big as you need. Next episode, the bugs that haunt every C programmer: leaks, dangling pointers, and double free. Ghost stories for coders. Keep coding, says Xecxec!

### Code shown

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int capacity = 2, count = 0;
    int *basket = calloc(capacity, sizeof(int));
    if (basket == NULL) {
        return 1;
    }
    printf("calloc gives: %d %d\n", basket[0], basket[1]);

    for (int fish = 10; fish <= 50; fish += 10) {
        if (count == capacity) {
            int new_capacity = capacity * 2;
            int *bigger = realloc(basket, new_capacity * sizeof(int));
            if (bigger == NULL) {
                free(basket);
                return 1;
            }
            basket = bigger;
            capacity = new_capacity;
            printf("Basket grown to %d\n", capacity);
        }
        basket[count] = fish;
        count++;
    }

    for (int i = 0; i < count; i++) {
        printf("%d ", basket[i]);
    }
    printf("\n");

    free(basket);
    return 0;
}
```

**Expected output:**

```text
calloc gives: 0 0
Basket grown to 4
Basket grown to 8
10 20 30 40 50 
```

### Bug of the Day

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int *basket = malloc(2 * sizeof(int));
    if (basket == NULL) return 1;
    basket[0] = 10;
    basket[1] = 20;

    basket = realloc(basket, 4 * sizeof(int));
    if (basket == NULL) {
        printf("realloc failed, and our 10 and 20 are lost!\n");
        return 1;
    }
    free(basket);
    return 0;
}
```

`gcc -Wall -Wextra bug.c` gives **no warning**, and on a normal run nothing goes wrong. The bug only shows when `realloc` fails: it returns `NULL`, which overwrites `basket`, so the original block (holding 10 and 20) can no longer be used or freed.

Fixed:

```c
    int *bigger = realloc(basket, 4 * sizeof(int));
    if (bigger == NULL) {
        free(basket);          /* old block is still valid here */
        return 1;
    }
    basket = bigger;
```

Why: on failure `realloc` leaves the old block alone and returns `NULL`, so assigning straight back to the only pointer throws that block away.

### Pun & challenge

- **Pun:** "realloc is like a Goan landlord: 'Need more space? Fine, but you might have to move house.'"
- **Challenge:** Start with room for 4 ints. Read numbers until `-1`, doubling with `realloc` (safe pattern) when full. Print the count and the numbers, then `free`.
- **Challenge answer:**

```c
int capacity = 4, count = 0, value;
int *list = malloc(capacity * sizeof(int));
if (list == NULL) return 1;

printf("Enter numbers, -1 to stop:\n");
while (scanf("%d", &value) == 1 && value != -1) {
    if (count == capacity) {
        int *bigger = realloc(list, capacity * 2 * sizeof(int));
        if (bigger == NULL) {
            free(list);
            return 1;
        }
        list = bigger;
        capacity *= 2;
    }
    list[count++] = value;
}

printf("You entered %d numbers:", count);
for (int i = 0; i < count; i++) {
    printf(" %d", list[i]);
}
printf("\n");
free(list);
/* input 5 8 13 21 34 55 -1 prints: You entered 6 numbers: 5 8 13 21 34 55 */
```

### Shorts for EP 67

**S1 · Your array can grow** — 0:25 · built from scenes 1 and 4

- **Hook (first 1.5s):** A fish basket overflowing: "Out of space? Get a bigger basket."
- **Script:** Normal C arrays can never change size. But heap memory can. realloc takes your old block and a new size. If there's room, it stretches the block. If not, it moves your data to a bigger block and gives you the new address. Your fish are never lost.
- **On-screen text:** realloc = BIGGER BASKET
- **Caption + hashtags:** Arrays that grow. #cprogramming #realloc #kodingkonkani #learntocode #ctutorial

**S2 · malloc vs calloc in 30s** — 0:30 · built from scene 3

- **Hook (first 1.5s):** Two blocks: "? ? ?" and "0 0 0".
- **Script:** malloc gives you memory but doesn't clean it, so it holds garbage until you fill it. calloc takes a count and a size, and sets every byte to zero. Need counters or totals that start at zero? Use calloc. Filling everything yourself right away? malloc is fine.
- **On-screen text:** malloc = DIRTY · calloc = CLEAN
- **Caption + hashtags:** Know the difference for your viva. #cprogramming #calloc #kodingkonkani #codingtips #malloc

**S3 · The realloc trap** — 0:35 · built from scene 9

- **Hook (first 1.5s):** `basket = realloc(basket, ...)` with a red underline.
- **Script:** basket equals realloc of basket. Looks fine, compiles fine. But if realloc fails, it returns NULL, and you just overwrote your only pointer to your data. Gone, and leaked. Always store the result in a temporary pointer first, check it, and only then update basket.
- **On-screen text:** NEVER p = realloc(p, ...)
- **Caption + hashtags:** One line, all your data gone. #cprogramming #debugging #kodingkonkani #realloc #cbugs

**S4 · The Goan landlord** — 0:15 · built from scene 7

- **Hook (first 1.5s):** Xecxec with a suitcase at a house door.
- **Script:** realloc is like a Goan landlord. Need more space? Fine. But you might have to move house.
- **On-screen text:** YOU MIGHT HAVE TO MOVE HOUSE
- **Caption + hashtags:** Every tenant knows this feeling. #programmerhumor #cprogramming #kodingkonkani #codingmemes #realloc

**S5 · Quiz: +1 or double?** — 0:25 · built from scene 8

- **Hook (first 1.5s):** "1,000 items. How many resizes?"
- **Script:** Your list starts with room for 1 item. You add 1,000 items. Growing by one each time, how many resizes? 999. Doubling each time? About 9. That's why real dynamic arrays double. Now build your own growing list. Comment your code.
- **On-screen text:** 999 vs 9
- **Caption + hashtags:** Work smarter, not harder. #cprogramming #codingquiz #kodingkonkani #realloc #learntocode

## EP 68 — Memory Bugs

**Module 10 · Dynamic memory · 7:30 · Mint + Tomato · Prerequisite: EP 67**

**Learning goals:** recognise the three classic heap bugs (memory leak, dangling pointer / use after free, double free) from a memory diagram; read GCC 13's `-Wuse-after-free` warning; protect yourself by setting a pointer to `NULL` after `free`; know that `free(NULL)` is safe.

### YouTube

- **Title:** The Ghost Pointer: 3 Memory Bugs in C | C EP 68
- **Description:** Leaks, dangling pointers and double free are the bugs that haunt every C programmer. We draw each one as a ghost in the heap, read GCC's warnings, crash a program on purpose, and learn the one-line habit that stops most of them. 0:00 Ghost story · 0:20 Title · 0:25 Bug 1: the leak · 1:10 Bug 2: the ghost pointer · 2:10 Bug 3: double free · 2:55 Code: the safe pattern · 4:15 Running it · 4:35 Pun · 4:40 Tools that catch ghosts · 5:15 Bug of the Day: use after free · 6:25 Challenge: find 3 bugs · 7:05 Module 10 complete
- **Tags:** memory leak c, dangling pointer c, use after free, double free c, free null pointer, wuse-after-free gcc, valgrind, address sanitizer, c memory bugs, learn c, koding konkani, c programming india
- **Thumbnail:** big text "GHOST POINTER"; a greyed-out heap box with a faint ghost-shaped arrow still pointing at it; a tomato "free()" stamp; Xecxec hiding behind a crate, scared; mint background, tomato text block

### Scene list

| # | Start | Length | Template | On screen | Animation & SFX |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00 | 0:20 | Concept slide | Night scene of an old Portuguese house in Fontainhas; a ghost floats past a door marked "Room returned" | Wind howl; lantern flicker; Xecxec peeks from behind a pillar |
| 2 | 0:20 | 0:05 | Title card | EP 68 · MEMORY BUGS | Title slams in; claw-click |
| 3 | 0:25 | 0:45 | Memory boxes | Heap block with no arrows pointing at it; label "LEAK: nobody can free me" | Stack frame vanishes taking its pointer; heap block left floating; slow fade to grey; lonely echo |
| 4 | 1:10 | 1:00 | Memory boxes | `ticket` at stack holding 0x7000; heap block 101 at 0x7000; after `free(ticket)` block is greyed but arrow remains as a dotted ghost arrow | Grey wash on free; arrow turns dotted and translucent; ghost "whoo"; claw knocks on the grey box, gets garbage |
| 5 | 2:10 | 0:45 | Memory boxes | Same grey block; `free(p)` called a second time; heap ledger shows the same entry twice | Ledger page tears; alarm; "double free detected" banner in tomato |
| 6 | 2:55 | 1:20 | Code explain | `safe.c` (22 lines); tracker: ticket, \*ticket | Butter highlights; after line 11 the ghost arrow is replaced with a NULL sign |
| 7 | 4:15 | 0:20 | Terminal | Compile and run | Three lines print; mint shield icon |
| 8 | 4:35 | 0:05 | Pun card | "Why are C programmers scared of ghosts? They have seen what a dangling pointer can do." | Card flips; Xecxec wears a bedsheet ghost costume; rimshot |
| 9 | 4:40 | 0:35 | Concept slide | Three tools: `gcc -Wall` (GCC 12+ use-after-free warnings), Valgrind (Linux/WSL), `-fsanitize=address` (Linux/WSL) | Tool icons slide in like ghost-hunting gear |
| 10 | 5:15 | 1:10 | Bug of the Day | `free(ticket); printf("%d", *ticket);` with GCC 13 warning, garbage output; then the double-free version crashing with "free(): double free detected in tcache 2" | Warning types out in butter; garbage number flickers; second part: crash banner; fix with `ticket = NULL;` slides in |
| 11 | 6:25 | 0:40 | Challenge | "Find 3 bugs" code card with 10 lines | Three magnifying glasses hover over the code; Xecxec holds a detective cap |
| 12 | 7:05 | 0:25 | Outro | "Module 10 complete!" badge; "Next: EP 69 · Files" | Badge stamps on; confetti; sign-off |

### Narration script

**\[1 · Ghost story\]** Old Goan houses have ghost stories. A family moves out, but late at night, someone still knocks on the door of the empty room. In C, the heap has ghosts too. Tonight, we meet three of them.

**\[2 · Title\]** Episode sixty-eight. Memory bugs.

**\[3 · Bug 1: the leak\]** The first ghost you already met in EP 66: the memory leak. A function mallocs a block, then returns without calling free. Its local pointer disappears with its stack frame. Look: the heap block is still there, but no arrow points at it. Nobody knows its address, so nobody can ever free it. It just floats there until the program ends. One leak is small. A leak inside a loop, or in a program that runs for days, eats all your RAM.

**\[4 · Bug 2: the ghost pointer\]** The second ghost is the scariest. Here's ticket, a pointer on the stack, pointing at a heap block holding 101. We call free of ticket. The block goes back to the heap. But look at ticket. It still holds the old address. free does not change your pointer. That arrow is now a ghost: it points at memory you no longer own. This is called a dangling pointer. If you read star ticket now, you are knocking on the door of a returned room. You might see 101, you might see garbage, and if the heap has given that memory to someone else, you might even change their data. This is called "use after free". It's one of the most common security bugs in real software.

**\[5 · Bug 3: double free\]** The third ghost: double free. You call free of p, and later, by mistake, free of p again. The heap keeps a ledger of what's been returned. Now the same block is being returned twice, which corrupts that ledger. Modern C libraries often catch this and stop the program on purpose, with a message like "double free detected". Sometimes they don't, and things go wrong much later.

**\[6 · Code: the safe pattern\]** Here's how to protect yourself. \[HL 5\] Line 5 mallocs one int for ticket. \[TRACK ticket=0x7000\] \[HL 6\] Line 6 checks for NULL, as always. \[HL 7\] Line 7 stores 101. \[TRACK \*ticket=101\] \[HL 8\] Line 8 prints it. \[HL 10\] Line 10: free of ticket. The block is returned. \[HL 11\] Line 11 is the magic line: ticket equals NULL. Watch the diagram. The ghost arrow disappears and becomes a NULL sign. \[TRACK ticket=NULL\] Now the pointer clearly says "nowhere". \[HL 13\] Line 13: if ticket is not NULL, use it. \[HL 14\] It is NULL, so line 14 is skipped, \[HL 16\] and line 16 prints "Ticket returned". The NULL check from EP 59 now works as a ghost detector. \[HL 19\] Line 19: free of ticket, again! Isn't that a double free? No. ticket is now NULL, and the C standard says free of NULL does nothing at all. So setting the pointer to NULL also protects you from double free. \[HL 20\] Line 20 prints a message to prove we're still alive. \[HL 21\] Return zero.

**\[7 · Running it\]** Compile and run. "Ticket: 101". "Ticket returned, pointer set to NULL". And "free of NULL is safe and does nothing". No crash, no ghosts. One line, ticket equals NULL, protects you from two of today's three bugs.

**\[8 · Pun\]** Why are C programmers scared of ghosts? Because they've seen what a dangling pointer can do.

**\[9 · Tools that catch ghosts\]** You don't have to hunt ghosts alone. First, always compile with dash Wall. GCC 12 and newer can warn about some use-after-free mistakes. Second, on Linux, or WSL on Windows, a tool called Valgrind runs your program and reports leaks and bad reads. Third, also on Linux or WSL, compile with dash f sanitize equals address. Your program then stops right at the bad line and tells you what went wrong. These are optional for now, but very useful when your projects get bigger.

**\[10 · Bug of the Day\]** Today's bug: use after free. Someone frees ticket, then prints star ticket. GCC 13 with dash Wall catches it: warning, pointer ticket used after free, and a note pointing at the free call. If you ignore it and run, you get a garbage number, because the heap has already reused that memory for its own bookkeeping. Now the double free version: free p, then free p again. GCC gives a similar used-after-free warning on the second free. And when you run it, the C library stops the program: "free: double free detected in tcache 2", then "Aborted". On Windows, the program usually just closes without a message. The fix for both: right after free, set the pointer to NULL. And don't use a pointer after you free it.

**\[11 · Challenge\]** Your final challenge for this module: be a ghost hunter. This short program has three memory bugs. Find all three, explain each in one line, and write the fixed version. Hint: one is about malloc's result, one is about a loop, and one is about the order of two lines. Pause and hunt.

**\[12 · Outro\]** That's Module 10 complete. Stack and heap, malloc, free, calloc, realloc, and now the ghosts. You can manage memory like a real C programmer. Next module, we save data to files, so it survives even after your program ends. Keep coding, says Xecxec!

### Code shown

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int *ticket = malloc(sizeof(int));
    if (ticket == NULL) return 1;
    *ticket = 101;
    printf("Ticket: %d\n", *ticket);

    free(ticket);
    ticket = NULL;

    if (ticket != NULL) {
        printf("Still have ticket %d\n", *ticket);
    } else {
        printf("Ticket returned, pointer set to NULL\n");
    }

    free(ticket);
    printf("free(NULL) is safe and does nothing\n");
    return 0;
}
```

**Expected output:**

```text
Ticket: 101
Ticket returned, pointer set to NULL
free(NULL) is safe and does nothing
```

### Bug of the Day

Part 1, use after free:

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int *ticket = malloc(sizeof(int));
    if (ticket == NULL) return 1;
    *ticket = 101;
    free(ticket);
    printf("Ticket: %d\n", *ticket);
    return 0;
}
```

GCC 13 (`gcc -Wall bug.c`) prints:

```text
bug.c: In function 'main':
bug.c:9:5: warning: pointer 'ticket' used after 'free' [-Wuse-after-free]
    9 |     printf("Ticket: %d\n", *ticket);
      |     ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
bug.c:8:5: note: call to 'free' here
    8 |     free(ticket);
      |     ^~~~~~~~~~~~
```

Running it prints a garbage value that changes each run, for example `Ticket: 1668369363` (it may also happen to print 101, which hides the bug).

Part 2, double free:

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int *p = malloc(sizeof(int));
    if (p == NULL) return 1;
    free(p);
    free(p);
    printf("Done\n");
    return 0;
}
```

GCC 13 warns `pointer 'p' used after 'free' [-Wuse-after-free]` on line 8. Running it on Linux (glibc) aborts:

```text
free(): double free detected in tcache 2
Aborted
```

On Windows the program usually exits silently.

Fixed (both):

```c
    free(ticket);
    ticket = NULL;   /* no ghost arrow; a second free(ticket) is now harmless */
```

Why: `free` returns the memory but leaves the old address in your pointer; setting it to `NULL` makes later mistakes detectable and makes a second `free` a no-op.

### Pun & challenge

- **Pun:** "Why are C programmers scared of ghosts? They have seen what a dangling pointer can do."
- **Challenge:** Find the 3 memory bugs in this program, explain each in one line, and fix it:

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int *scores = malloc(3 * sizeof(int));
    for (int i = 0; i <= 3; i++) {
        scores[i] = i * 10;
    }
    free(scores);
    printf("%d\n", scores[0]);
    return 0;
}
```

- **Challenge answer:** (1) The `malloc` result is never checked for NULL. (2) `i <= 3` writes `scores[3]`, one past the end of a 3-int block (heap overflow). (3) `scores[0]` is read after `free` (use after free; GCC 13 warns with `-Wuse-after-free`). Fixed:

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int *scores = malloc(3 * sizeof(int));
    if (scores == NULL) return 1;
    for (int i = 0; i < 3; i++) {
        scores[i] = i * 10;
    }
    printf("%d\n", scores[0]);
    free(scores);
    scores = NULL;
    return 0;
}
```

```text
0
```

### Shorts for EP 68

**S1 · The ghost pointer** — 0:30 · built from scenes 1 and 4

- **Hook (first 1.5s):** A dotted ghost arrow pointing at a grey box: "This pointer is dead. It doesn't know."
- **Script:** You call free on a pointer. The memory goes back to the heap. But your pointer still holds the old address. It's a ghost, pointing at a room you've already returned. Read through it, and you get garbage, or worse. Fix: right after free, set the pointer to NULL.
- **On-screen text:** free() DOES NOT CLEAR YOUR POINTER
- **Caption + hashtags:** The scariest bug in C. #cprogramming #pointers #kodingkonkani #learntocode #memorybugs

**S2 · 3 memory bugs in 30 seconds** — 0:30 · built from scenes 3–5

- **Hook (first 1.5s):** Three ghosts line up: LEAK, DANGLING, DOUBLE FREE.
- **Script:** Leak: you forgot to free, and lost the address. Dangling pointer: you freed it but kept using the old address. Double free: you freed the same block twice. The one habit that helps with two of them: free, then set the pointer to NULL.
- **On-screen text:** LEAK · DANGLING · DOUBLE FREE
- **Caption + hashtags:** Know your ghosts. #cprogramming #memory #kodingkonkani #codingtips #memorybugs

**S3 · double free detected** — 0:30 · built from scene 10

- **Hook (first 1.5s):** Terminal: "free(): double free detected in tcache 2 / Aborted".
- **Script:** free p. Then free p again. GCC 13 warns: pointer used after free. Run it on Linux and the program is killed: double free detected. Fix it with one line after the first free: p equals NULL. Freeing NULL is completely safe, it does nothing.
- **On-screen text:** free(NULL) IS SAFE
- **Caption + hashtags:** One line saves you. #cprogramming #debugging #kodingkonkani #doublefree #cbugs

**S4 · Scared of ghosts** — 0:12 · built from scene 8

- **Hook (first 1.5s):** Xecxec in a bedsheet ghost costume.
- **Script:** Why are C programmers scared of ghosts? Because they've seen what a dangling pointer can do.
- **On-screen text:** THEY'VE SEEN A DANGLING POINTER
- **Caption + hashtags:** Happy haunting. #programmerhumor #cprogramming #kodingkonkani #codingmemes #pointers

**S5 · Find 3 bugs** — 0:35 · built from scene 11

- **Hook (first 1.5s):** 10 lines of code and three magnifying glasses: "Three bugs. Can you find them?"
- **Script:** This program mallocs three ints, fills them in a loop, frees them and prints the first. It has three memory bugs. Hint one: what if malloc fails? Hint two: count the loop. Hint three: look at the order of the last two lines. Comment all three to become a ghost hunter.
- **On-screen text:** FIND 3 BUGS
- **Caption + hashtags:** Only real ghost hunters get all three. #cprogramming #codingchallenge #kodingkonkani #memorybugs #learntocode
