import dspy
from lm import lm
from schema import CHARACTER_CARD_SCHEMA

def character_card_generation(context: str):
    """
    Generates a detailed character card from provided context using a chain-of-thought approach.
    
    Args:
        context (str): Raw context data about the character
        
    Returns:
        CharacterCard: A structured character card with formatted fields
    """
    schema_string = " -> ".join(["context", ", ".join(f"{k}: {v}" for k, v in CHARACTER_CARD_SCHEMA.items())])
    cot = dspy.ChainOfThought(schema_string)
    
    return cot(context=f"""
        Based on this context create a detailed character card:
        
        <context>
        {context}
        </context>

        Generate a character card that captures:
        1. Character's title/name
        2. Key section headings
        3. Important entities and their relationships
        4. Biographical information
        5. Background lore
        6. Character knowledge
        7. Example messages/conversations
        8. Example posts/statements
        9. Main topics/themes
        10. Communication style patterns
        11. Characteristic adjectives

        Ensure all content maintains consistency with the character's established personality and background.
    """)


with open("context/chromia.txt", "r") as file:
    chromia_txt = file.read()

class Notetaker:
    def __init__(self):
        self.story_parts = []

    def update(self, message, speaker):
        prompt = (
            f"As a storyteller, based on the following message by {speaker}, "
            f"continue developing the character's backstory:\n\n"
            f"Message:\n{message}\n\n"
            f"Character's Story Update:"
        )
        story_update = lm(prompt, temperature=0.3)
        self.story_parts.append(story_update[0].strip())

    def get_full_story(self):
        return "\n".join(self.story_parts)

def simulate_conversation(goal: str, char1, char2, turns=5):
    conversation = []
    current_speaker = char1
    last_response = (
        f"Let's discuss: {goal}.\n"
        f"Here's some context about Chromia:\n{chromia_txt}"
    )
    notetaker = Notetaker()

    for _ in range(turns):
        prompt = (
            f"{current_speaker['name']} ({current_speaker['style']}):\n{last_response}"
        )
        response = lm(prompt, temperature=current_speaker['temperature'])
        conversation.append({"speaker": current_speaker['name'], "text": response})
        notetaker.update(response, current_speaker['name'])
        last_response = response
        current_speaker = char2 if current_speaker == char1 else char1
        print(f"{conversation[-1]['speaker']} ({current_speaker['style']}): {response}")

    # Generate character card from the full conversation
    full_story = notetaker.get_full_story()
    character_card = character_card_generation(full_story)

    # Save outputs
    with open("result.txt", "w") as f:
        for entry in conversation:
            f.write(f"{entry['speaker']}: {entry['text']}\n")

    with open("character_card.txt", "w") as f:
        f.write(str(character_card))

    with open("scratchpad.txt", "w") as f:
        f.write(full_story)

    return conversation, character_card