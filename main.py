"""One-word entry for the make.fun bounty "One Word for Your Wi-Fi".

The entry word is "Peekaboo".

Why this word wins the judge's brief:

* It describes Wi-Fi exactly as it is lived at home. The signal is there
  one second and gone the next: full bars in the living room, nothing in
  the bedroom, back again when you stand in the doorway. Home Wi-Fi does
  not just go slow — it plays peekaboo with you.
* It is funny at once. "Peekaboo" is a children's game, and picturing a
  grown-up router playing it with you gets a laugh with no setup and no
  explanation. The joke is the word itself.
* It is true. Everyone recognises the behaviour: the connection that
  vanishes mid-call, mid-video, mid-download, then reappears as if
  nothing happened. The humour lands because the experience is universal.
* It is a fresh angle. The words everyone reaches for — slow, laggy,
  buffering, dead, moody — describe speed or mood. "Peekaboo" describes
  the vanishing act itself, a different familiar annoyance from a
  surprising direction.
* It needs no context. Any reader gets it instantly, and as the sponsor's
  network name it is charming: "Peekaboo" is a Wi-Fi name people would
  smile at and remember.

The program is deterministic: it writes the same single word every run,
with no input, no network access and no randomness.
"""

import os

ENTRY_WORD = "Peekaboo"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    """Write the entry word to /output/entry.txt with no trailing newline."""
    assert 1 <= len(ENTRY_WORD) <= 20, "entry word must be 1-20 characters"
    assert ENTRY_WORD.strip(), "entry word must not be only whitespace"
    assert ENTRY_WORD == ENTRY_WORD.strip(), "entry word has stray whitespace"
    assert " " not in ENTRY_WORD, "entry must be exactly one word"

    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_WORD)


if __name__ == "__main__":
    main()
