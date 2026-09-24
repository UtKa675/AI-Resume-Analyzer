import streamlit as st
from resume_parser import extract_text_from_pdf
from skill_extractor import extract_skills
from matcher import calculate_skill_match, semantic_similarity
from recommender import generate_recommendations

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.main {
    background-color: #0e1117;
}

.hero {
    padding: 25px 0 10px 0;
}

.hero h1 {
    font-size: 45px;
    margin-bottom: 5px;
}

.hero p {
    font-size: 18px;
    color: #a0a0a0;
}

.section-title {
    font-size: 24px;
    font-weight: 700;
    margin-top: 25px;
}

.skill-box {
    background-color: #f1f5f9;
    color: #111827;
    padding: 12px 16px;
    border-radius: 10px;
    margin: 5px 0;
    border: 1px solid #e2e8f0;
}

.metric-card {
    background-color: #1f2937;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)


# ---------------- HEADER ----------------

st.markdown("""
<div class="hero">
    <h1>📄 AI Resume Analyzer</h1>
    <p>
        Analyze your resume against a job description using NLP,
        skill matching and semantic similarity.
    </p>
</div>
""", unsafe_allow_html=True)

st.divider()


# ---------------- INPUT SECTION ----------------

col1, col2 = st.columns(2)

with col1:
    st.subheader("📄 Upload Resume")

    resume_file = st.file_uploader(
        "Upload your resume in PDF format",
        type=["pdf"]
    )

with col2:
    st.subheader("💼 Job Description")

    job_description = st.text_area(
        "Paste the complete job description",
        height=220,
        placeholder="Paste job description here..."
    )


st.write("")


# ---------------- ANALYZE BUTTON ----------------

if st.button(
    "🚀 Analyze Resume",
    use_container_width=True,
    type="primary"
):

    if not resume_file:
        st.warning("⚠️ Please upload your resume.")
        st.stop()

    if not job_description.strip():
        st.warning("⚠️ Please paste a job description.")
        st.stop()

    with st.spinner("🔍 Analyzing your resume..."):

        # Extract resume text
        resume_text = extract_text_from_pdf(resume_file)

        if not resume_text.strip():
            st.error(
                "❌ Could not extract text from this PDF. "
                "Please upload a text-based PDF."
            )
            st.stop()

        # Extract skills
        resume_skills = extract_skills(resume_text)
        jd_skills = extract_skills(job_description)

        # Calculate skill match
        score, matched, missing = calculate_skill_match(
            resume_skills,
            jd_skills
        )

        # Semantic similarity
        semantic_score = semantic_similarity(
            resume_text,
            job_description
        )

        # Recommendations
        recommendations = generate_recommendations(
            resume_skills,
            missing,
            resume_text
        )

    # ---------------- RESULTS ----------------

    st.divider()

    st.markdown(
        '<div class="section-title">📊 Analysis Overview</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "🎯 Skill Match",
            f"{score:.1f}%"
        )

    with col2:
        st.metric(
            "🧠 Semantic Similarity",
            f"{semantic_score:.1f}%"
        )

    with col3:
        st.metric(
            "🔎 Skills Detected",
            len(resume_skills)
        )


    # ---------------- PROGRESS ----------------

    st.write("")

    st.subheader("🎯 Skill Match Score")

    st.progress(
        min(score / 100, 1.0)
    )


    # ---------------- MATCHED SKILLS ----------------

    st.subheader("✅ Matched Skills")

    if matched:

        for skill in sorted(matched):
            st.markdown(
                f"""
                <div class="skill-box">
                    ✅ {skill}
                </div>
                """,
                unsafe_allow_html=True
            )

    else:
        st.info("No matching skills detected.")


    # ---------------- MISSING SKILLS ----------------

    st.subheader("⚠️ Missing Skills")

    if missing:

        for skill in sorted(missing):
            st.markdown(
                f"""
                <div class="skill-box">
                    ⚠️ {skill}
                </div>
                """,
                unsafe_allow_html=True
            )

    else:
        st.success(
            "🎉 No missing skills detected from the configured skill list."
        )


    # ---------------- RESUME SKILLS ----------------

    st.subheader("🧠 Skills Detected in Resume")

    if resume_skills:

        st.write(
            ", ".join(sorted(resume_skills))
        )

    else:

        st.info(
            "No configured skills were detected."
        )


    # ---------------- RECOMMENDATIONS ----------------

    st.subheader("💡 Resume Recommendations")

    for recommendation in recommendations:

        st.info(
            recommendation
        )


    # ---------------- EXTRACTED TEXT ----------------

    with st.expander("🔎 View Extracted Resume Text"):

        st.text(
            resume_text
        )


    # ---------------- JOB SKILLS ----------------

    with st.expander("📚 Skills Detected in Job Description"):

        st.write(
            ", ".join(sorted(jd_skills))
            if jd_skills
            else "No configured skills detected."
        )


# ---------------- FOOTER ----------------

st.divider()

st.caption(
    "AI Resume Analyzer • NLP + Skill Matching + TF-IDF Similarity"
)

st.caption(
    "For learning and portfolio purposes. "
    "The score is an automated similarity indicator, not an official ATS decision."
)