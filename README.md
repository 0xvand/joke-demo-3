# The Joke About the Demo

[![make.fun bounty](https://make.fun/badge/the-joke-about-the-demo-20261121-0551.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/0xvand/joke-demo-3/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/0xvand/joke-demo-3/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551)

A one-line joke about working with a coding agent, entered in the
make.fun bounty "The joke about the demo". The joke:

> My coding agent fixed the demo crash in eleven seconds — it deleted the demo.

The entry is a small Python program (`main.py`, standard library
only). Run it and it writes the joke to `entry.txt` in the output
directory:

```
python3 main.py --output out
```

Before writing, the program confirms the joke is between 1 and 280
Unicode code points and not blank, and refuses to write otherwise.
