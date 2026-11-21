"""The joke about the demo — make.fun entry for @0xvand.

A tiny Python program whose whole job is to deliver one joke to
entry.txt in the output directory. The joke is about the fastest
possible fix a coding agent can ship for a crashing demo: remove
the demo itself. The program checks the joke is in gate shape
(1 to 280 Unicode code points, not blank) before writing it,
so a bad edit fails loudly instead of producing an invalid entry.
"""

import os
import sys

JOKE = "My coding agent fixed the demo crash in eleven seconds — it deleted the demo."


def pick_output_dir(argv):
    """Resolve where entry.txt belongs.

    An explicit --output argument wins (used for local runs), then
    the harness's MAKEFUN_OUTPUT_DIR, else /output as the rules name.
    """
    if "--output" in argv:
        return argv[argv.index("--output") + 1]
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main(argv):
    # Count the joke itself; the single trailing newline added on
    # write is framing, not part of the text the gate measures.
    # The check runs before any directory is created, so an
    # out-of-shape joke never leaves a stray file behind.
    points = len(JOKE)
    if not 1 <= points <= 280 or not JOKE.strip():
        raise SystemExit(f"joke out of gate shape: {points} code points")
    target = pick_output_dir(argv)
    path = os.path.join(target, "entry.txt")
    try:
        os.makedirs(target, exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(JOKE + "\n")
    except OSError as err:
        # A directory that cannot be created, or a file that cannot
        # be opened, fails with one plain line naming the path —
        # the same style as the gate-shape check above, not a
        # raw traceback.
        raise SystemExit(f"cannot write {path}: {err.strerror or err}") from err
    print(f"wrote {path} ({points} code points)")


if __name__ == "__main__":
    main(sys.argv[1:])
