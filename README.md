# 🧾 Receipt Parser & Analyzer

A full-stack mini-app to upload, parse, and analyze bills/receipts with OCR and analytics.

## 📦 Features
- Upload `.jpg`, `.pdf`, `.png`, `.txt` receipts
- OCR using Tesseract + rule-based parsing
- FastAPI backend with SQLite storage
- Search, sort, and aggregate expenditures
- Streamlit dashboard to visualize results

## 🚀 Setup Instructions

1. Clone repo and install dependencies:
```bash
pip install -r requirements.txt
```

2. Start the backend:
```bash
uvicorn api.main:app --reload
```

3. Start the Streamlit UI:
```bash
streamlit run ui/app.py
```

4. Upload a file and explore the parsed data!

## 📁 Project Structure

- `backend/`: OCR parsing, data models, database setup
- `api/`: FastAPI routes
- `ui/`: Streamlit app
- `data/`: Sample test files (optional)

## 📊 Analytics
- Total/average spend
- Vendor frequency distribution
- Monthly spend trend (extendable)

---
✅ Built for Python Internship – R1 Full Stack Task
