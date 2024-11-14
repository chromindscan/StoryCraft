# StoryCraft
At Chromia, we are accelerating our efforts and are determined to contribute to the Crypto x AI space as a “Brain” layer for AI agents. This initiative is built on top of ChromindScan. In this project, we would like to showcase how 2 AI agents are able to talk to each other. By being given a goal and some context about the project, the AI agents are able to complete the task and create an Eliza-compatible (https://github.com/ai16z/eliza) character card.

![](logo.jpg)

# How it works
We let the 2 different AI Agents talk freely with each other using x number of rounds, with a note taker taking notes on the back story based on the goal and context. Then the AI Agent will clean up and generate a formatted Eliza compatible character card.


# Roadmap
- [ ] Adding Memories, Logs, Goals to make Chromia + ChromindScan compatible to Eliza
- [ ] Deploy AlphaOnChain with Eliza

# Setup

1. Create a Python Virtual Environment
It’s recommended to use a virtual environment to manage dependencies.

```
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
```

2. Install Dependencies

Install the required Python packages using pip:
```
pip install -r requirements.txt
```

3. Set Up Environment Variables (.env)

```
cp .env.sample .env
```


4. Prepare Context and Configuration Files

**context/context.txt**

This file provides background information for the AI agents to understand the context of the conversation.

**config.json**

Parameters:
- goal: The objective of the AI agents’ conversation.
- turns: The number of turns the agents will converse.
- character1 and character2: Define the attributes of each AI agent.
- name: The agent’s name.
- style: Describes how the agent communicates.
- personality: Provides depth to the agent’s character.
- temperature: Controls the randomness of the AI’s responses (range 0 to 2).

5. Running the Program

```
python main.py
```

After running the script, three files will be generated:
1.	result.txt: Contains the full conversation between the two AI agents.
2.	scratchpad.txt: Contains the compiled backstory generated by the notetaker AI.
3.	character_card.txt: Contains the final Eliza-compatible character card.
