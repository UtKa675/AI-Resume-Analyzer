def generate_recommendations(resume_skills, missing_skills, resume_text):
    recommendations = []

    if missing_skills:
        top_missing = sorted(missing_skills)[:5]
        recommendations.append(
            "Review the job requirements and, if you genuinely have these skills, "
            f"make them explicit in your resume: {', '.join(top_missing)}."
        )
    else:
        recommendations.append(
            "The configured required skills were detected in the resume."
        )

    if len(resume_text.split()) < 150:
        recommendations.append(
            "Your extracted resume text is quite short. Check whether the PDF "
            "contains selectable text and whether important sections are missing."
        )

    if "python" in resume_skills and "sql" in resume_skills:
        recommendations.append(
            "Consider highlighting a project that demonstrates Python and SQL together."
        )

    recommendations.append(
        "Use measurable outcomes in project descriptions where they are truthful, "
        "for example processing time, dataset size, accuracy, or automation impact."
    )

    return recommendations
