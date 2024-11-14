CHARACTER_CARD_SCHEMA = {
    "title": "str",
    "name": "str",
    "headings": "list[str]",
    "entities_and_metadata": "list[dict[str, str]]",
    "bio": "list[str]",
    "lore": "list[str]",
    "knowledge": "list[str]",
    "messageExamples": "list[list[dict[str, dict[str, str]]]]",
    "postExamples": "list[str]",
    "topics": "list[str]",
    "style": "dict[str, list[str]]",
    "adjectives": "list[str]"
}