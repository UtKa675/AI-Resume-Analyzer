import streamlit as st
from resume_parser import extract_text_from_pdf
from skill_extractor import extract_skills
from matcher import calculate_skill_match, semantic_similarity
from recommender import generate_recommendations

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")
st.write("Upload a resume and compare it with a job description.")

resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_description = st.text_area(
    "Paste Job Description",
    height=220,
    placeholder="Paste the complete job description here..."
)

if st.button("🚀 Analyze Resume", use_container_width=True):
    if not resume_file:
        st.warning("Please upload a PDF resume.")
        st.stop()

    if not job_description.strip():
        st.warning("Please paste a job description.")
        st.stop()

    with st.spinner("Analyzing resume..."):
        resume_text = extract_text_from_pdf(resume_file)

        if not resume_text.strip():
            st.error("Could not extract text from this PDF. Try a text-based PDF.")
            st.stop()

        resume_skills = extract_skills(resume_text)
        jd_skills = extract_skills(job_description)

        score, matched, missing = calculate_skill_match(
            resume_skills, jd_skills
        )

        semantic_score = semantic_similarity(
            resume_text, job_description
        )

        recommendations = generate_recommendations(
            resume_skills, missing, resume_text
        )

    st.divider()

    c1, c2, c3 = st.columns(3)
    c1.metric("Skill Match", f"{score:.1f}%")
    c2.metric("Semantic Similarity", f"{semantic_score:.1f}%")
    c3.metric("Skills Found", len(resume_skills))

    st.subheader("✅ Matched Skills")
    if matched:
        st.write(", ".join(sorted(matched)))
    else:
        st.info("No matching skills detected.")

    st.subheader("⚠️ Missing Skills")
    if missing:
        st.write(", ".join(sorted(missing)))
    else:
        st.success("No missing skills detected from the configured skill list.")

    st.subheader("🧠 Skills Detected in Resume")
    if resume_skills:
        st.write(", ".join(sorted(resume_skills)))
    else:
        st.info("No configured skills were detected.")

    st.subheader("💡 Recommendations")
    for recommendation in recommendations:
        st.write(f"• {recommendation}")

    with st.expander("🔎 Extracted Resume Text"):
        st.text(resume_text)

    with st.expander("📚 Detected Skills in Job Description"):
        st.write(", ".join(sorted(jd_skills)) if jd_skills else "No configured skills detected.")

st.caption("Note: This is a learning/portfolio project. The score is an automated similarity indicator, not an official ATS or hiring decision.")
