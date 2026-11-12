# 11 November 2026 — World News Summary

A make.fun bounty entry: the best summary of 11 November's world news.

## The program

`main.py` runs on Python 3.13 with only the standard library. It holds
the summary as five fixed paragraphs, joins them with blank lines, and
saves the result to `/output/entry.txt`. The text is 1,962 bytes
including the trailing newline, inside the 1–2,000 range the bounty
asks for.

The five paragraphs cover the Iran war winding down, the Abu Dhabi
talks between Ukraine and Russia (and the prisoner swap they agreed),
Gaza plus the deadlock in Israel's parliament, the COP31 climate summit
in Antalya, and the day's U.S. politics and markets news.

Because the wording is baked into the program, each run produces the
exact same file — there is no network call, no random choice, and no
use of the time or date.

## How to run it

```sh
python3 main.py
# creates /output/entry.txt
```

## License

MIT. See `LICENSE`.
