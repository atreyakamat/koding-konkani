import { classifyError, type Excerpt } from "./errorExcerpt.ts";

/** Hand-written Bug-of-the-Day panels for the two bugs whose Bible text has nothing to show
 * (prose only, no output and no crash message). Everything else follows the rules in errorExcerpt.ts.
 *  - lines: what the panel shows (empty for a hang: the panel is a prompt with a blinking cursor).
 *  - hang: terminal panel with `$ ./program`, a blinking cursor and ^C after a pause.
 *  - caption: small line under the panel. */
export type BugOverride = { lines: string[]; hang?: boolean; caption?: string };

export const BUG_OVERRIDES: Record<number, BugOverride> = {
  // EP67: first clause of "The bug only shows when realloc fails: it returns NULL, which overwrites basket..."
  67: { lines: ["realloc returns NULL and overwrites basket"] },
  // EP73: the binary search never ends; there is nothing to print.
  73: { lines: [], hang: true, caption: "no output, program hangs" },
};

export type BugPanel = Excerpt | { kind: "override"; lines: string[]; override: BugOverride };

/** What the Bug-of-the-Day panel shows for an episode: its override if it has one, else the excerpt rules. */
export const bugPanel = (ep: number, error: string): BugPanel => {
  const override = BUG_OVERRIDES[ep];
  return override ? { kind: "override", lines: override.lines, override } : classifyError(error);
};
