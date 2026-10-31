import { AbsoluteFill, Series } from "remotion";
import { palette } from "../theme/palette";
import { coloursForModule } from "../theme/modules";
import {
  TitleCard,
  ConceptSlide,
  CodeExplain,
  MemoryBoxes,
  Terminal,
  AlgorithmBars,
  BugOfTheDay,
  PunCard,
  Challenge,
  Outro,
  ShortLayout,
} from "../scenes";

const BUBBLE_SORT_C = `#include <stdio.h>
#include <stdbool.h>

void print_array(const int a[], int n) {
    for (int i = 0; i < n; i++)
        printf("%d ", a[i]);
    printf("\\n");
}

void bubble_sort(int a[], int n) {
    for (int pass = 0; pass < n - 1; pass++) {
        bool swapped = false;
        for (int j = 0; j < n - 1 - pass; j++) {
            if (a[j] > a[j + 1]) {
                int temp = a[j];
                a[j] = a[j + 1];
                a[j + 1] = temp;
                swapped = true;
            }
        }
        printf("After pass %d: ", pass + 1);
        print_array(a, n);
        if (!swapped)
            break;
    }
}

int main(void) {
    int marks[] = {5, 2, 9, 1, 6, 3};
    int n = sizeof(marks) / sizeof(marks[0]);

    printf("Before:       ");
    print_array(marks, n);
    bubble_sort(marks, n);
    return 0;
}`;

// Trimmed to the buggy fragment (marks[7] holds a 7th sentinel slot so the overrun is visible);
// the full reproduction with its #include and print loop lives in docs/bible/m12.md.
const BUBBLE_BUG_WRONG = `int marks[7] = {5, 2, 9, 1, 6, 3, -1};
int n = 6;

for (int pass = 0; pass < n - 1; pass++) {
    for (int j = 0; j < n - pass; j++) {
        if (marks[j] > marks[j + 1]) {
            int temp = marks[j];
            marks[j] = marks[j + 1];
            marks[j + 1] = temp;
        }
    }
}`;

const BUBBLE_BUG_FIXED = BUBBLE_BUG_WRONG.replace(
  "for (int j = 0; j < n - pass; j++) {",
  "for (int j = 0; j < n - 1 - pass; j++) {",
);

const HI_C = `#include <stdio.h>

int main() {
    printf("Hi");
    return 0;
}`;

/** Each entry: how long it plays (frames @30fps) and the element itself. */
type GalleryItem = { name: string; durationInFrames: number; element: React.ReactNode };

/** ShortLayout is authored for a 1080x1920 canvas; scale it to fit the gallery's 1920x1080 frame. */
const SHORT_SCALE = 1080 / 1920;
const SHORT_SCALED_WIDTH = 1080 * SHORT_SCALE;
const ShortPreviewFrame: React.FC<{ children: React.ReactNode }> = ({ children }) => (
  <AbsoluteFill style={{ background: palette.ink }}>
    <div
      style={{
        position: "absolute",
        top: 0,
        left: (1920 - SHORT_SCALED_WIDTH) / 2,
        width: 1080,
        height: 1920,
        // `scale` with a bare number is unreliable here (React treats unrecognized CSS
        // properties' numeric values as needing a unit), so `transform` is the safe form.
        transform: `scale(${SHORT_SCALE})`,
        transformOrigin: "top left",
        overflow: "hidden",
      }}
    >
      {children}
    </div>
  </AbsoluteFill>
);

const ep01Items = (bg: string, accent: string): GalleryItem[] => {
  const colours = { bg, accent };
  return [
    {
      name: "TitleCard",
      durationInFrames: 90,
      element: (
        <TitleCard
          durationInFrames={90}
          colours={colours}
          ep={1}
          title="Welcome to Koding Konkani"
          moduleLabel="M00"
        />
      ),
    },
    {
      name: "ConceptSlide",
      durationInFrames: 150,
      element: (
        <ConceptSlide
          durationInFrames={150}
          colours={colours}
          heading="How to study"
          lines={[
            "Type every program yourself. No copy-paste.",
            "Break things on purpose, then read the error.",
            "If you're stuck, rewind. Nobody is grading replays.",
          ]}
          analogy={{
            title: "Why it sticks",
            body: "Five minutes of practice beats an hour of watching.",
          }}
        />
      ),
    },
    {
      name: "CodeExplain",
      durationInFrames: 180,
      element: (
        <CodeExplain
          durationInFrames={180}
          colours={colours}
          file="hi.c"
          source={HI_C}
          labels={{ 4: "function · text in quotes · end of statement" }}
        />
      ),
    },
    {
      name: "MemoryBoxes",
      durationInFrames: 150,
      element: (
        <MemoryBoxes
          durationInFrames={150}
          colours={colours}
          boxes={[
            { name: "x", value: "42", address: "0x7ffee4" },
            { name: "ptr", value: "0x7ffee4", address: "0x7fffa0", isPointer: true, pointsTo: "x" },
          ]}
        />
      ),
    },
    {
      name: "Terminal",
      durationInFrames: 150,
      element: (
        <Terminal
          durationInFrames={150}
          colours={colours}
          lines={[
            { text: "gcc hi.c -o hi", kind: "input" },
            { text: "./hi", kind: "input" },
            { text: "Hi", kind: "success" },
          ]}
        />
      ),
    },
    {
      name: "AlgorithmBars",
      durationInFrames: 180,
      element: (
        <AlgorithmBars
          durationInFrames={180}
          colours={colours}
          trace={[
            { step: "1.1", array: [5, 2, 9, 1, 6, 3], compare: [0, 1], swap: [0, 1] },
            { step: "1.2", array: [2, 5, 9, 1, 6, 3], compare: [1, 2] },
            { step: "1.3", array: [2, 5, 1, 9, 6, 3], compare: [2, 3], swap: [2, 3] },
            { step: "1.4", array: [2, 5, 1, 6, 9, 3], compare: [3, 4], swap: [3, 4] },
            { step: "1.5", array: [2, 5, 1, 6, 3, 9], compare: [4, 5], swap: [4, 5], sorted: [5] },
          ]}
        />
      ),
    },
    {
      name: "BugOfTheDay",
      durationInFrames: 210,
      element: (
        <BugOfTheDay
          durationInFrames={210}
          colours={colours}
          wrongCode={`#include <stdio.h>\n\nint main() {\n    printf(“Hi”);\n    return 0;\n}`}
          error={"hi.c:4:12: error: stray '\\342' in program\n    4 |     printf(“Hi”);"}
          fixedCode={HI_C}
          why="C only understands the straight double quote from your keyboard; curly quotes from websites are different characters."
        />
      ),
    },
    {
      name: "PunCard",
      durationInFrames: 120,
      element: (
        <PunCard
          durationInFrames={120}
          colours={colours}
          pun="Why do C programmers never get lost? They always know where their pointers are."
        />
      ),
    },
    {
      name: "Challenge",
      durationInFrames: 150,
      element: (
        <Challenge
          durationInFrames={150}
          colours={colours}
          task="Comment: why are you learning C?"
          examples={["exams", "a job", "a game"]}
        />
      ),
    },
    {
      name: "Outro",
      durationInFrames: 150,
      element: (
        <Outro durationInFrames={150} colours={colours} nextEp={2} nextTitle="What is C, really?" />
      ),
    },
    {
      name: "ShortLayout",
      durationInFrames: 150,
      element: (
        <ShortPreviewFrame>
          <ShortLayout
            durationInFrames={150}
            colours={colours}
            ep={1}
            hook="A crab will teach you C?"
            visualLabel={'Xecxec points a claw at printf("Hi");'}
            caption="Meet Xecxec, your new C teacher."
          />
        </ShortPreviewFrame>
      ),
    },
  ];
};

const ep74Items = (bg: string, accent: string): GalleryItem[] => {
  const colours = { bg, accent };
  return [
    {
      name: "TitleCard",
      durationInFrames: 90,
      element: (
        <TitleCard
          durationInFrames={90}
          colours={colours}
          ep={74}
          title="Bubble Sort"
          moduleLabel="M12"
        />
      ),
    },
    {
      name: "ConceptSlide",
      durationInFrames: 150,
      element: (
        <ConceptSlide
          durationInFrames={150}
          colours={colours}
          heading="Complexity"
          lines={[
            "Compare neighbours. If left is bigger than right, swap.",
            "Best O(n), average O(n²), worst O(n²) (reverse order); space O(1) extra; stable.",
            "If a whole pass makes zero swaps, the array is sorted. Stop early.",
          ]}
          analogy={{
            title: "Think of it like",
            body: "Soda bubbles: the biggest one always reaches the top first.",
          }}
        />
      ),
    },
    {
      name: "CodeExplain",
      durationInFrames: 260,
      element: (
        <CodeExplain
          durationInFrames={260}
          colours={colours}
          file="bubble.c"
          source={BUBBLE_SORT_C}
          labels={{
            11: "outer loop counts passes",
            13: "inner loop: n - 1 - pass, because j+1 must stay in bounds",
            14: "compare neighbours",
            18: "swapped = true",
          }}
        />
      ),
    },
    {
      name: "MemoryBoxes",
      durationInFrames: 150,
      element: (
        <MemoryBoxes
          durationInFrames={150}
          colours={colours}
          boxes={[
            { name: "a", value: "0x4000", address: "0x7ffee0" },
            { name: "n", value: "6", address: "0x7ffee8" },
            { name: "temp", value: "5", address: "0x7ffeec" },
          ]}
        />
      ),
    },
    {
      name: "Terminal",
      durationInFrames: 180,
      element: (
        <Terminal
          durationInFrames={180}
          colours={colours}
          lines={[
            { text: "gcc bubble.c -o bubble", kind: "input" },
            { text: "./bubble", kind: "input" },
            { text: "Before:       5 2 9 1 6 3", kind: "output" },
            { text: "After pass 1: 2 5 1 6 3 9", kind: "output" },
            { text: "After pass 4: 1 2 3 5 6 9", kind: "success" },
          ]}
        />
      ),
    },
    {
      name: "AlgorithmBars",
      durationInFrames: 180,
      element: (
        <AlgorithmBars
          durationInFrames={180}
          colours={colours}
          trace={[
            { step: "1.1", array: [5, 2, 9, 1, 6, 3], compare: [0, 1], swap: [0, 1] },
            { step: "1.2", array: [2, 5, 9, 1, 6, 3], compare: [1, 2] },
            { step: "1.3", array: [2, 5, 1, 9, 6, 3], compare: [2, 3], swap: [2, 3] },
            { step: "1.4", array: [2, 5, 1, 6, 9, 3], compare: [3, 4], swap: [3, 4] },
            { step: "1.5", array: [2, 5, 1, 6, 3, 9], compare: [4, 5], swap: [4, 5], sorted: [5] },
          ]}
        />
      ),
    },
    {
      name: "BugOfTheDay",
      durationInFrames: 240,
      element: (
        <BugOfTheDay
          durationInFrames={240}
          colours={colours}
          wrongCode={BUBBLE_BUG_WRONG}
          error={"No error or warning from GCC. Output:\n1 -1 2 3 5 6"}
          fixedCode={BUBBLE_BUG_FIXED}
          why="With j < n - pass, j reaches n - 1 and marks[j + 1] reads one element past the data."
        />
      ),
    },
    {
      name: "PunCard",
      durationInFrames: 120,
      element: (
        <PunCard
          durationInFrames={120}
          colours={colours}
          pun="Why did bubble sort go to the gym? It wanted to swap its weight around."
        />
      ),
    },
    {
      name: "Challenge",
      durationInFrames: 150,
      element: (
        <Challenge
          durationInFrames={150}
          colours={colours}
          task="Sort these marks in descending order: 72, 45, 98, 60, 85."
          examples={["72", "45", "98", "60", "85"]}
        />
      ),
    },
    {
      name: "Outro",
      durationInFrames: 150,
      element: (
        <Outro durationInFrames={150} colours={colours} nextEp={75} nextTitle="Selection sort" />
      ),
    },
    {
      name: "ShortLayout",
      durationInFrames: 150,
      element: (
        <ShortPreviewFrame>
          <ShortLayout
            durationInFrames={150}
            colours={colours}
            ep={74}
            hook="Watch the biggest bubble."
            visualLabel="Six bars; the tallest floats to the end on every pass."
            caption="Sorting, but make it soda."
          />
        </ShortPreviewFrame>
      ),
    },
  ];
};

const m0 = coloursForModule(0);
const m12 = coloursForModule(12);

const GALLERY: GalleryItem[] = [...ep01Items(m0.bg, m0.accent), ...ep74Items(m12.bg, m12.accent)];

/** Total duration of the gallery, for the Composition's durationInFrames. */
export const SCENE_GALLERY_DURATION = GALLERY.reduce((sum, item) => sum + item.durationInFrames, 0);

/** Plays every scene template once per episode (EP 01, then EP 74), each in its real module colourway. */
export const SceneGallery: React.FC = () => {
  return (
    <AbsoluteFill style={{ background: "black" }}>
      <Series>
        {GALLERY.map((item, index) => (
          <Series.Sequence
            key={`${item.name}-${index}`}
            durationInFrames={item.durationInFrames}
            name={item.name}
          >
            {item.element}
          </Series.Sequence>
        ))}
      </Series>
    </AbsoluteFill>
  );
};
