
# 🕵️ Police PDF Search Tool

This is a simple, browser-based tool designed to help police officials quickly search through PDF circulars, notices, or official documents using keywords.

## 🔍 What This Tool Does

- Upload any number of PDF documents (e.g., notices, circulars, advisories)
- Search using a keyword like **"snake"**, **"curfew"**, or **"schedule"**
- Get instant results sorted by **most recent**
- Click to **download** or **view** the matched PDF

---

## 🚓 How Police Officials Can Use It

### If Hosted Online (Recommended)
1. Visit the tool link in your browser: `https://your-app-url.streamlit.app` *(to be updated after deployment)*
2. Upload PDF files using the file uploader section.
3. Enter a search word (e.g., "wildlife", "emergency").
4. View matched documents and download them directly.

### If Running Locally (Offline Mode)
1. Install required tools (one-time setup):
    ```bash
    pip install streamlit PyPDF2 pandas
    ```
2. Run the tool:
    ```bash
    streamlit run app.py
    ```
3. It will open automatically in your browser.

---

## 📁 Project Structure

```
pdf_search_app/
│
├── app.py             # Main Streamlit app
├── pdfs/              # Folder to hold uploaded PDFs
└── README.md          # This instruction manual
```

---

## 📸 Screenshots (Add Yours)

- Example search result for keyword: `snake`
- Upload interface

---

## 🔐 Data Privacy Note

- This tool runs locally or securely online.
- No document is shared outside unless explicitly downloaded.
- Safe for departmental use.

---

## 🙏 Acknowledgment

Created to assist [Your Police Department Name] with quick access to critical PDF documents.
