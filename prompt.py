import dspy
from lm import lm

def character_card_generation(context: str):
    cot = dspy.ChainOfThought("text -> title: str, headings: list[str], entities_and_metadata: list[dict[str, str]], bio: list[str], lore: list[str], knowledge: list[str], messageExamples: list[list[dict[str, dict[str, str]]]], postExamples: list[str], topics: list[str], style: dict[str, list[str]], adjectives: list[str]")
    return cot(text=f"""Based on this context create a character card
<context>
{context}
</context>

Ensure that all content is consistent with the character's personality and background as described in the context.
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

    full_story = notetaker.get_full_story()

    with open("result.txt", "w") as f:
        for entry in conversation:
            f.write(f"{entry['speaker']}: {entry['text']}\n")

    with open("scratchpad.txt", "w") as f:
        f.write(full_story)

    return conversation