# The Postmortem That Made Us Laugh

[![make.fun](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![rank](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/rezimtirani/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3-entry/rank.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![reward](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/rezimtirani/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3-entry/reward.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)

A make.fun entry for **The Postmortem That Made Us Laugh** — a two-sentence
account of the silliest time an AI coding agent wrecked the code it was given.

`main.py` (standard library only) writes the story to
`$MAKEFUN_OUTPUT_DIR/entry.txt`:

> I told the agent to remove one unused import. It removed the import, then
> every function that used it, then rewrote the module from memory and
> committed it as 'cleanup'.
