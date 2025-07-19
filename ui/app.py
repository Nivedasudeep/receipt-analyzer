import streamlit as st
import re
from datetime import datetime

st.set_page_config(page_title="Receipt Uploader & Visualizer")

st.title("📄 Receipt Uploader & Visualizer")
st.markdown("Upload Receipt (`.jpg`, `.pdf`, `.png`, `.txt`)")

uploaded_file = st.file_uploader(
    "Drag and drop file here",
    type=["jpg", "png", "pdf", "txt", "jpeg"]
)

def extract_info(text):
    vendor = re.search(r"(?i)(vendor|biller)[:\-]?\s*(.+)", text)
    amount = re.search(r"(?i)(total|amount)[:\-]?\s*₹?\$?([\d,]+\.\d{2})", text)
    date = re.search(r"(?i)(date|billing period)[:\-]?\s*(\d{2}[\/\-]\d{2}[\/\-]\d{4})", text)

    return {
        "Vendor": vendor.group(2).strip() if vendor else "Not found",
        "Amount": amount.group(2).strip() if amount else "Not found",
        "Date": date.group(2).strip() if date else "Not found"
    }

if uploaded_file:
    file_contents = uploaded_file.read().decode("utf-8", errors="ignore")
    extracted_data = extract_info(file_contents)

    st.subheader("📋 Extracted Information")
    st.write(f"**Vendor:** {extracted_data['Vendor']}")
    st.write(f"**Amount:** ₹{extracted_data['Amount']}")
    st.write(f"**Date:** {extracted_data['Date']}")

    st.success("✅ File processed successfully.")
