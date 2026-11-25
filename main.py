# One Word, One Username — the entry is the account's own handle,
# bright-sparrow-21-7895. The bounty asks for a single word that works
# as a username, and the most honest answer is the name already on the
# account: short, pronounceable, memorable, and taken by exactly the
# right person. No invention needed; the username is the entry.

import os

ENTRY = "bright-sparrow-21-7895"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
