import fitz


def extract_text_from_pdf(pdf_file):
    """Extract text from an uploaded PDF using PyMuPDF."""
    text = ""

    pdf = fitz.open(stream=pdf_file.read(), filetype="pdf")

    for page in pdf:
        text += page.get_text("text") + "\n"

    pdf.close()

    return text
