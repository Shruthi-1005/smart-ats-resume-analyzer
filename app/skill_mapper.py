import json
import string

with open("data/skills.json", "r") as file:
    SKILLS = json.load(file)

SYNONYMS = {
    "object oriented programming": "oop",
    "object-oriented programming": "oop",
    "oops": "oop",
    "data structures and algorithms": "dsa",
    "problem-solving": "problem solving",
    "rest api": "api",
    "communication skills": "communication"
}


def clean_text(text: str):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))

    for word, replacement in SYNONYMS.items():
        text = text.replace(word, replacement)

    return text


def extract_skills(text: str):
    text = clean_text(text)

    found_skills = []

    for skill in SKILLS:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))
