# AI Resume Analyzer

A Python + NLP portfolio project that compares a resume PDF with a job description.

## Features

- Upload PDF resume
- Extract text from PDF
- Detect configured skills
- Compare resume skills with job requirements
- Calculate skill overlap
- Calculate TF-IDF cosine similarity
- Show matched and missing skills
- Generate basic recommendations
- Streamlit web interface

## Tech Stack

- Python
- Streamlit
- PyMuPDF
- scikit-learn
- Regular Expressions
- JSON

## Run

Create and activate a virtual environment, then:

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Important

This is a learning/portfolio project. The displayed percentages are automated similarity indicators and are not official ATS scores or hiring decisions.

## Future upgrades

1. spaCy NLP pipeline
2. Better skill/entity extraction
3. Sentence Transformer embeddings
4. LLM-generated feedback
5. Resume section detection
6. OCR for scanned PDFs
7. Unit tests
8. Deployment
