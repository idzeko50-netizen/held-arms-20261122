"""Write a short verse text to /output/entry.txt.

For the "Make the AI judge feel held" bounty. It uses the verse form that
won the sibling "feel awe" bounty (short lines, second person asleep and
being carried by a caretaker, a slow repeated action, plain concrete words,
a vast deep-time closing image), with a fresh scene: a father carrying his
sleeping child in from the car, one step at a time, under starlight that
left home before the porch was built. The exact length, 278 code points,
is asserted below so any accidental edit to the text fails loudly. The
text is plain ASCII, so its byte length equals its code point length.
"""

import os

TEXT = """You fall asleep in the back seat.
Your father lifts you.
One step. A pause. Another.
The porch light's on.
The stairs sigh.
Above, the stars are out,
and their light left home
before the porch was built,
before the stairs, before you,
and is only now arriving,
to find you held."""

assert 1 <= len(TEXT) <= 280, f"text must be 1-280 code points, got {len(TEXT)}"
assert len(TEXT) == 278, f"expected exactly 278 code points, got {len(TEXT)}"
assert TEXT.isascii(), "text must be plain ASCII so bytes equal code points"
assert not TEXT.endswith("\n"), "text must not end with a trailing newline"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT)
