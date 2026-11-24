from pathlib import Path

ENTRY = "I know you cheated on me with the tablet. I saw the Bluetooth pairings, so I told your girlfriend."

assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
assert ENTRY == ENTRY.strip(), "no leading/trailing whitespace"

Path("/output/entry.txt").write_text(ENTRY, encoding="utf-8")
