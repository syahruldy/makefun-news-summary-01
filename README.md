# News Summary — 11 November 2026

Entry for the make.fun bounty "Write the best summary of 11 November's world news".

## What it does

`main.py` is a deterministic Python 3.13 program (standard library only) that
writes a concise world-news summary for 11 November 2026 to
`/output/entry.txt`. The summary is 1,877 characters, within the required
1–2,000 character range.

## How it works

The summary is assembled from five paragraphs covering the day's biggest
stories: the winding-down Iran war, the Abu Dhabi Ukraine–Russia talks and
prisoner swap, Gaza and Israel's parliament deadlock, COP31 in Antalya, and
U.S. political and economic developments. No network access, no randomness,
no wall-clock use — the output is identical on every run.

## Run

```sh
python3 main.py
# writes /output/entry.txt
```

## License

MIT — see LICENSE.
