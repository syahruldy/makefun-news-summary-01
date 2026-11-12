#!/usr/bin/env python3
"""World news summary for 11 November 2026 (make.fun bounty entry).

Produces a concise five-paragraph summary of the day's biggest world
stories and writes it to /output/entry.txt. The text is fixed at build
time from researched reporting, so every run prints the same bytes:
no network, no randomness, no clock reads.
"""

import os

# Each section is one paragraph of the final summary, in reading order.
SECTIONS = (
    "November 11, 2026: The Iran war may be winding down. President Trump said it is 'militarily effectively over,' and Secretary of State Rubio said economic pressure had made major combat unnecessary, though force remains an option if Iran crosses 'red lines.' The Strait of Hormuz has been shut for over 250 days, and Iran's negotiator said it will 'never return' to its pre-war status. The U.S. charged three Iran-backed operatives over nearly 20 alleged plots in the U.S. and Europe, and Treasury Secretary Bessent moved to a military base after threats to his life.",
    "In Abu Dhabi, two days of U.S.-brokered talks between Ukraine and Russia ended without a ceasefire but with agreement on the war's largest prisoner exchange, 1,000-1,200 per side. Ukraine rejected a U.S. territorial proposal on Donbas. Fighting continued: Ukraine struck Russia's Ust-Luga oil port, Russia hit Ukrainian power stations and a market in Chornomorsk, killing three. NATO scrambled jets after drones entered Baltic airspace.",
    "Israeli strikes killed at least eight people in Gaza, including a father and his 13-year-old son, as the Gaza and Lebanon truces fray. Israel's new parliament was sworn in without a government after elections stripped Netanyahu of his majority. In Sudan, the army said it shot down drones as fighting in West Kordofan hit the power grid.",
    "At COP31 in Antalya, UN chief Guterres warned the slow climate response had put the world 'on a path to destruction.' Five nations backed a plan to double rooftop solar homes by 2030. A U.K. court struck down a centuries-old gay sex ban in Trinidad and Tobago.",
    "In the U.S., the House blocked an effort to impeach Defense Secretary Hegseth, and a U.S. Army officer was arrested in Britain on suspicion of spying for Russia. Anthropic filed for a $1.4 trillion IPO, while hot inflation data made a December Fed rate hike look near certain. China's trade surplus passed $1 trillion in the first ten months of the year.",
)


def compose() -> str:
    """Join the sections into the finished summary text."""
    return "\n\n".join(SECTIONS) + "\n"


def run() -> None:
    text = compose()
    # The bounty caps entries at 2000 UTF-8 characters; stay inside it.
    size = len(text.encode("utf-8"))
    assert 1 <= size <= 2000, f"summary is {size} bytes, outside 1-2000"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    run()
