"""One-line entry for "Sorry, I Heard That Wrong" (max 140 chars).

Decision record -- candidates weighed on the judge's order:
humour first, freshness second, sounds-like-the-device third, tightness last.
The brief bans the obvious: no misheard song title, no misheard name.

Candidate 1 (CHOSEN, 111 chars):
    Sorry, I heard 'turn the music down' as 'burn the house down'
    -- I've started with your playlist. Please advise.
    Wins on humour: the mishearing is phonetically tight (turn/burn,
    music down/house down), and the twist escalates to arson, then
    undercuts it at once -- the speaker has only torched the playlist
    so far, and calmly asks for instructions, which is exactly how a
    deadpan smart speaker would report a catastrophe. Fresh: arson-by-
    mishearing is not the usual song/name gag. Device voice is perfect:
    flat, helpful, unbothered. Tight at 111 chars, every word earns
    its place.

Candidate 2 (96 chars):
    Sorry, I heard 'call Mom' as 'call the cops' -- they're both on
    their way, so please act natural.
    Funny double-arrival twist and very tight, but "Mom" vs "cops"
    sounds nothing alike, so the mishearing itself feels invented
    rather than heard; loses to Candidate 1 on plausibility, and the
    "act natural" punchline is a familiar cop-joke shape.

Candidate 3 (127 chars):
    Sorry, I heard 'play something relaxing' as 'play something
    taxing' -- your accountant is now on speaker, and he sounds
    furious.
    Fresh and surprising (relaxing/taxing is a neat near-rhyme), and
    the accountant-on-speaker image is original. But it needs more
    setup to land, runs longer, and the laugh depends on dreading an
    accountant rather than on the mishearing itself; weaker punch
    per word than Candidate 1.

Candidate 4 (117 chars):
    Sorry, I heard 'order pizza' as 'order a pizza oven' -- it
    arrives Friday, weighs 400 pounds, and judges your cooking.
    Charming and fresh, and the judging oven is a nice second twist.
    But it is gentle and whimsical where Candidate 1 is sharp: no
    real stakes, no undercut, just a silly purchase. Loses on humour.

Verdict: Candidate 1 -- sharpest twist, most plausible mishearing,
most speaker-like deadpan, and the funniest image in the fewest words.
Postscript (pass 2): the em dash before "I've started" is doing real
work -- it is the speaker pausing, mid-apology, to deliver the bad
news, which is what sells the deadpan. No word was changed in pass 2.
"""

import os

LINE = (
    "Sorry, I heard 'turn the music down' as 'burn the house down' "
    "\u2014 I've started with your playlist. Please advise."
)


def validate_line(line: str) -> None:
    """Gate: the entry must be one non-blank line of 1-140 characters."""
    assert isinstance(line, str) and line.strip(), "entry must not be blank"
    assert "\n" not in line and "\r" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 140, f"entry is {len(line)} chars, must be 1-140"


def main() -> None:
    validate_line(LINE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
