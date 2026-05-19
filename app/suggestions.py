def generate_suggestions(missing_skills):
    suggestions = []

    skill_tips = {
        "sql": "Add SQL or database-related project experience.",
        "oop": "Mention OOP concepts or OOP-based project work.",
        "sdlc": "Add SDLC understanding in skills section.",
        "dbms": "Include DBMS or database handling experience.",
        "communication": "Mention presentations, teamwork, or communication skills."
    }

    for skill in missing_skills:
        if skill in skill_tips:
            suggestions.append(skill_tips[skill])

    return suggestions