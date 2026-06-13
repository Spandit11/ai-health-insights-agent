def validate_pdf(uploaded_file):

    if uploaded_file is None:
        return False, "No file selected"

    if uploaded_file.size > 20 * 1024 * 1024:
        return False, "File exceeds 20 MB limit"

    if not uploaded_file.name.lower().endswith(".pdf"):
        return False, "Only PDF files are allowed"

    return True, "Valid PDF"