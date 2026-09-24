import json
import re


def load_skills():
    with open("data/skills.json", "r", encoding="utf-8") as file:
        return json.load(file)


def normalize_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9+#.\s-]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text


def extract_skills(text):
    """
    Detect skills from a configurable skill dictionary.
    This is a baseline keyword-based NLP approach.
    """
    normalized = normalize_text(text)
    skills_data = load_skills()

    found_skills = set()

    for category, skills in skills_data.items():
        for skill in skills:
            skill_normalized = normalize_text(skill)

            pattern = r"(?<!\w)" + re.escape(skill_normalized) + r"(?!\w)"

            if re.search(pattern, normalized):
                found_skills.add(skill)

    return found_skills
