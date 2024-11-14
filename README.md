# StoryCraft
At Chromia, we are accelerating our efforts and are determined to contribute to the Crypto x AI space as a “Brain” layer for AI agents. This initiative is built on top of ChromindScan. In this project, we would like to showcase how 2 AI agents are able to talk to each other. By being given a goal and some context about the project, the AI agents are able to complete the task and create an Eliza-compatible character card.

# How it works
We let the 2 different AI Agents talk freely with each other using x number of rounds, with a note taker taking notes on the back story based on the goal and context. Then the AI Agent will clean up and generate a formatted Eliza compatible character card.


# Roadmap
- [ ] Adding Memories, Logs, Goals to make Chromia + ChromindScan compatible to Eliza
- [ ] Deploy AlphaOnChain with Eliza

# How to run it

1. Setup python environment & install all dependencies
```
python -m venv .venv
source .venv/bin/activate
```

2. Setup `.env`


3. Setup `context/context.txt` file and `config.json`


4. Run `python main.py`