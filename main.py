"""Loading Screen Gold: A Tip in 200 Characters.

Writes one original loading-screen tip (1-200 UTF-8 characters) to
/output/entry.txt. Stdlib only, no network, no secrets.
"""

import os

TIP = (
    "Loading\u2026 Your AI agent just refactored the code, ran the tests, "
    "and is now Googling its own error message. "
    "Give it a minute. Take one yourself."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TIP)


if __name__ == "__main__":
    main()
