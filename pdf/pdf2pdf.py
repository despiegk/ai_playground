import PyPDF2
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO
from pprint import pprint; import IPython

def remove_images_from_pdf(input_pdf_path, output_pdf_path):
    # Read the existing PDF
    input_pdf = PyPDF2.PdfReader(open(input_pdf_path, "rb"))

    # Create a new PDF
    output_pdf = PyPDF2.PdfWriter()

    for page_num in range(len(input_pdf.pages)):
        # Extract text from the page
        page = input_pdf.pages[page_num]
        text = page.extract_text()


        IPython.embed()

        # Create a PDF page with text
        packet = BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)
        can.drawString(10, 800, text)  # You might need to adjust positioning
        can.save()

        # Move the "packet" to the beginning
        packet.seek(0)
        new_pdf = PyPDF2.PdfReader(packet)

        # Add the page to the output
        output_pdf.add_page(new_pdf.pages[0])

    # Write the output PDF
    with open(output_pdf_path, "wb") as output_file:
        output_pdf.write(output_file)

# Example usage

# Example usage
remove_images_from_pdf('/Users/despiegk1/Downloads/OurWorld Venture Creator Investor Intro - Aug 2023 v5.8 (1).pdf', 
                '/Users/despiegk1/Documents/ourworld_venturecreator_intro.pdf')
