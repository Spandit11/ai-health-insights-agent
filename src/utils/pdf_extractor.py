import pdfplumber


def extract_text_from_pdf(uploaded_file):

    extracted_text = ""

    with pdfplumber.open(uploaded_file) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                extracted_text += page_text + "\n"

    return extracted_text