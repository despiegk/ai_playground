import PyPDF2
import nltk
from nltk.tokenize import sent_tokenize
from typing import List
from pprint import pprint; import IPython

import pdfplumber

def extract_text_from_pdf(pdf_path):
    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            # Extracting text
            text += page.extract_text(x_tolerance=1, y_tolerance=3)
            print(text)
            # Extracting table data if present
            tables = page.extract_tables()
            for table in tables:
                # Formatting each row in the table
                for row in table:
                    print(row)
                    formatted_row = " | ".join(str(cell) if cell is not None else '' for cell in row)
                    text += "\n" + formatted_row
                text += "\n\n"  # Extra newline after each table for separation

    return text

# Example usage
extract_text_from_pdf('/Users/despiegk1/Downloads/humania.pdf')
