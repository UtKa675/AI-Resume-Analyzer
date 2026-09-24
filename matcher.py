def calculate_skill_match(resume_skills, job_skills):
    """
    Calculate overlap between resume skills and required job skills.
    """
    resume_skills = set(resume_skills)
    job_skills = set(job_skills)

    matched = resume_skills.intersection(job_skills)
    missing = job_skills.difference(resume_skills)

    if not job_skills:
        return 0.0, matched, missing

    score = len(matched) / len(job_skills) * 100

    return score, matched, missing


def semantic_similarity(resume_text, job_description):
    """
    Optional semantic similarity using TF-IDF + cosine similarity.
    Falls back to 0 if the documents cannot be vectorized.
    """
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity

    documents = [resume_text, job_description]

    try:
        vectorizer = TfidfVectorizer(stop_words="english")
        matrix = vectorizer.fit_transform(documents)

        similarity = cosine_similarity(matrix[0:1], matrix[1:2])[0][0]

        return similarity * 100
    except ValueError:
        return 0.0
