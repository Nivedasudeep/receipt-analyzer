import re
import pytesseract
from PIL import Image
import fitz  # PyMuPDF

CURRENCY_MAP = {'$': 'USD', '₹': 'INR', '€': 'EUR', '£': 'GBP'}

def extract_text(path):
    if path.endswith(('.jpg', '.png')):
        return pytesseract.image_to_string(Image.open(path), lang='eng+hin+fra')
    elif path.endswith('.pdf'):
        doc = fitz.open(path)
        text = " ".join(page.get_text() for page in doc)
        doc.close()
        return text
    elif path.endswith('.txt'):
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    return ""

def parse_file(path):
    text = extract_text(path)
    if not text: return None
    vendor_match = re.search(r'(?i)(?:from|vendor)[:\s]*([\w\s&.,-]+)', text)
    date_match = re.search(r'(\d{2}[\/\-]\d{2}[\/\-]\d{4})', text)
    amount_match = re.search(r'([₹$€£]?[\s]?[0-9]+(?:[,.][0-9]+)?)', text)
    vendor = vendor_match.group(1).strip() if vendor_match else "Unknown Vendor"
    date = date_match.group(1) if date_match else None
    raw_amount = amount_match.group(1).strip() if amount_match else "0"
    currency_symbol = re.findall(r'[₹$€£]', raw_amount)
    currency = CURRENCY_MAP.get(currency_symbol[0], 'UNKNOWN') if currency_symbol else 'UNKNOWN'
    amount = float(re.sub(r'[₹$€£,\s]', '', raw_amount)) if raw_amount else 0.0
    vendor_lower = vendor.lower()
    if 'electricity' in vendor_lower: category = 'Utilities'
    elif 'amazon' in vendor_lower or 'flipkart' in vendor_lower: category = 'Shopping'
    elif 'internet' in vendor_lower or 'jio' in vendor_lower: category = 'Internet'
    elif 'grocery' in vendor_lower or 'mart' in vendor_lower: category = 'Groceries'
    else: category = 'Other'
    return {'vendor': vendor, 'date': date, 'amount': amount, 'currency': currency, 'category': category}
