
import streamlit as st
import os
import re
from datetime import datetime
from PyPDF2 import PdfReader
import pandas as pd

# Directory to store PDFs
PDF_DIR = "pdfs"
os.makedirs(PDF_DIR, exist_ok=True)

# Function to extract excerpts with keyword context
def extract_excerpts(filepath, keyword, window=40):
    reader = PdfReader(filepath)
    full_text = " ".join([page.extract_text() for page in reader.pages if page.extract_text()])
    excerpts = []
    for match in re.finditer(keyword, full_text, re.IGNORECASE):
        start = max(match.start() - window, 0)
        end = min(match.end() + window, len(full_text))
        excerpt = full_text[start:end].replace('\n', ' ').strip()
        excerpts.append(excerpt)
    return excerpts

# Streamlit app
st.title("🔍 Police PDF Search Tool with Excerpts")
st.write("Upload PDFs and search for keywords. Relevant excerpts from documents will be shown.")

# Upload PDFs
uploaded_files = st.file_uploader("Upload PDF files", type="pdf", accept_multiple_files=True)
if uploaded_files:
    for file in uploaded_files:
        with open(os.path.join(PDF_DIR, file.name), "wb") as f:
            f.write(file.read())

# Search input
keyword = st.text_input("Enter keyword to search:")

# Process search
if keyword:
    results = []
    for filename in os.listdir(PDF_DIR):
        if filename.endswith(".pdf"):
            path = os.path.join(PDF_DIR, filename)
            excerpts = extract_excerpts(path, keyword)
            if excerpts:
                for excerpt in excerpts:
                    results.append({
                        "filename": filename,
                        "excerpt": excerpt
                    })

    if results:
        st.subheader(f"Results for '{keyword}':")
        for res in results:
            st.markdown(f"**{res['filename']}**")
            st.write(res['excerpt'])
            st.markdown("---")
    else:
        st.warning("No matching excerpts found in any PDF.")
