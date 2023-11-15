import PyPDF2
import nltk
from nltk.tokenize import sent_tokenize
from typing import List
from pprint import pprint; import IPython

nltk.download('punkt')

def group_sentences_to_paragraphs(sentences: List[str], max_paragraph_length: int = 30) -> List[str]:
    paragraphs = []
    paragraph = []

    for sentence in sentences:
        paragraph.append(sentence)
        if len(paragraph) >= max_paragraph_length or sentence.endswith('.'):
            paragraphs.append(' '.join(paragraph))
            paragraph = []

    # Add the last paragraph if it's not empty
    if paragraph:
        paragraphs.append(' '.join(paragraph))

    return paragraphs

def pdf_to_markdown(pdf_path: str, markdown_path: str) -> None:
    # Open the PDF file
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)

        # Read each page and extract text
        text = ""
        for page in range(num_pages):
            text += reader.pages[page].extract_text() + "\n"

        # Use NLTK to split text into sentences
        sentences = sent_tokenize(text)
        
        IPython.embed()

        # Group sentences into paragraphs
        paragraphs = group_sentences_to_paragraphs(sentences)

        # Write to Markdown file
        with open(markdown_path, 'w', encoding='utf-8') as md_file:
            for para in paragraphs:
                md_file.write(para + "\n\n")

# Example usage
pdf_to_markdown('/Users/despiegk1/Downloads/H.U.M.A.N.I.A - Universal Abundance on the Horizon (1).pdf', 
                '/Users/despiegk1/Documents/humana.md')
