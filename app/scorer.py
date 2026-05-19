def calculate_score(matched, total_skills):
    if total_skills == 0:
        return 0

    score = (len(matched) / total_skills) * 100

    return round(score, 2)