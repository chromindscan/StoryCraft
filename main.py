from dotenv import load_dotenv
load_dotenv()

from prompt import simulate_conversation

character1 = {
    "name": "Adam",
    "style": "utopian, optimistic, degenerate",
    "personality": "wise and thoughtful, full of energy, like to use crypto slangs, love database and blockchain as transparency and security are important to him.",
    "scratchpad": "",
    "temperature": 1.0
}

character2 = {
    "name": "Eve",
    "style": "dystopian, pessimistic, worried",
    "personality": "cynical and sarcastic, bipolar, like to use crypto slangs, had existential crisis",
    "temperature": 1.0
}

goal = "create a new AI character for Chromia branding with backstory"
simulate_conversation(
    goal=goal,
    char1=character1,
    char2=character2,
    turns=3
)



