import json
from pathlib import Path
from typing import Dict, Any
from dotenv import load_dotenv
load_dotenv()

from prompt import simulate_conversation

def load_config() -> Dict[str, Any]:
    config_path = Path(__file__).parent / "config.json"
    with open(config_path, "r") as f:
        return json.load(f)

# Load configuration
config = load_config()
character1 = config["characters"]["adam"]
character2 = config["characters"]["eve"]
goal = config["goals"]["chromia_character"]

simulate_conversation(
    goal=goal,
    char1=character1,
    char2=character2,
    turns=3
)


