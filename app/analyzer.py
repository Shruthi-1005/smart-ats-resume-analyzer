from app.skill_mapper import extract_skills
from app.matcher import match_skills
from app.scorer import calculate_score
from app.suggestions import generate_suggestions


def analyze_resume(resume_text, job_description):
    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(job_description)

    matched, missing = match_skills(resume_skills, jd_skills)

    ats_score = calculate_score(matched, len(jd_skills))

    suggestions = generate_suggestions(missing)

    return {
        "ats_score": ats_score,
        "matched_skills": matched,
        "missing_skills": missing,
        "suggestions": suggestions
    }