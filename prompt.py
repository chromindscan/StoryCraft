import dspy
from lm import lm
from schema import CHARACTER_CARD_SCHEMA

def character_card_generation(context: str):
    """
    Generates a detailed character card from provided context.
    
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


with open("context/context.txt", "r") as file:
    context_txt = file.read()

class Notetaker:
    def __init__(self):
        self.story_parts = []

    def update(self, message, speaker):
        prompt = (
            f"As a storyteller, based on the following message by {speaker}, "
            
            f"Continue developing the character's backstory:\n\n"
            
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
    last_response = f"Let's discuss: {goal}.\n{context_txt}"
    notetaker = Notetaker()
    
    import json

    print(f"\n[Conversation: {char1['name']} and {char2['name']} discuss {goal}]\n")

    for _ in range(turns):
        prompt = f"{current_speaker['name']} ({current_speaker['style']}):\n{last_response}"
        response = lm(prompt, temperature=current_speaker['temperature'])
        
        print(f"{current_speaker['name']}: {response}\n")
        
        conversation.append({"speaker": current_speaker['name'], "text": response})
        notetaker.update(response, current_speaker['name'])
        last_response = response
        current_speaker = char2 if current_speaker == char1 else char1

    full_story = notetaker.get_full_story()
    character_card = character_card_generation(full_story)

    with open("result.txt", "w") as f:
        for entry in conversation:
            f.write(f"{entry['speaker']}: {entry['text']}\n")

    with open("character_card.json", "w") as f:
        character_card_dict = {
            field: getattr(character_card, field)
            for field in CHARACTER_CARD_SCHEMA.keys()
        }
        json.dump(character_card_dict, f, indent=2)

    with open("scratchpad.txt", "w") as f:
        f.write(full_story)

    return conversation, character_card