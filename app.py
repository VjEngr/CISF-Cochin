
import streamlit as st
import os
import re
from datetime import datetime
from PyPDF2 import PdfReader
import pandas as pd

# Directory to store PDFs
PDF_DIR = "pdfs"
os.makedirs(PDF_DIR, exist_ok=True)

# Function to extract text and simulate date from filename
def extract_pdf_info(filepath):
    reader = PdfReader(filepath)
    text = " ".join([page.extract_text() for page in reader.pages if page.extract_text()])
    match = re.search(r'\\d{4}-\\d{2}-\\d{2}', os.path.basename(filepath))
    date = datetime.strptime(match.group(), "%Y-%m-%d") if match else datetime(1900, 1, 1)
    return {"filename": os.path.basename(filepath), "text": text, "date": date, "path": filepath}

# Upload PDFs
st.title("🔍 Police Notices Search Tool")
st.write("Upload PDFs of circulars or notices. Then search for keywords.")

uploaded_files = st.file_uploader("Upload PDF files", type="pdf", accept_multiple_files=True)
if uploaded_files:
    for file in uploaded_files:
        with open(os.path.join(PDF_DIR, file.name), "wb") as f:
            f.write(file.read())

# Load and process PDFs
pdf_data = []
for filename in os.listdir(PDF_DIR):
    if filename.endswith(".pdf"):
        info = extract_pdf_info(os.path.join(PDF_DIR, filename))
        pdf_data.append(info)
df = pd.DataFrame(pdf_data)

# Keyword search
keyword = st.text_input("Enter keyword to search:")
if keyword:
    keyword = keyword.lower()
    results = df[df['text'].str.lower().str.contains(keyword, na=False)]
    results = results.sort_values(by="date", ascending=False)
    st.subheader(f"Results for '{keyword}'")
    for _, row in results.iterrows():
        st.markdown(f"**{row['filename']}** – {row['date'].date()}")
        st.markdown(f"📄 [Download PDF](file://{row['path']})")
        st.markdown("---")
    if results.empty:
        st.warning("No matching documents found.")
