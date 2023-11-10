"""
PDF Page Extraction and Concatenation Script

Overview:
The PDF Page Extraction and Concatenation Script is a Python program designed to extract specific pages from multiple PDF files and concatenate them into a single PDF file. This script is particularly useful when you need to compile selected pages from different PDF documents into a cohesive and organized output.

Usage:

Prerequisites:
Make sure you have Python installed on your system. Additionally, install the required library using:
```bash
pip install PyPDF2
"""

import PyPDF2

def extract_and_concatenate_pdfs(input_pdfs, page_numbers, output_pdf):
    merged_pdf_writer = PyPDF2.PdfWriter()

    for i, pdf_file in enumerate(input_pdfs):
        with open(pdf_file, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page_num in page_numbers[i]:
                page = pdf_reader.pages[page_num - 1]
                merged_pdf_writer.add_page(page)

    with open(output_pdf, 'wb') as output_file:
        merged_pdf_writer.write(output_file)

if __name__ == "__main__":
    # Replace these file names with your actual file names
    input_pdfs = ['1.pdf', '2.pdf', '3.pdf', '4.pdf']

    # Specify the page numbers to extract from each PDF as a list
    # For example, [[page_num1, page_num2, ...], [page_num1, page_num2, ...], ...]
    page_numbers = [
        [19,28,37],  # Page numbers for file1.pdf
        [15,16,28,40,59],     # Page numbers for file2.pdf
        [16,31,70,91,154,187],        # Page numbers for file3.pdf
        [33,67,99]         # Page numbers for file4.pdf
    ]

    output_pdf = 'output.pdf'

    extract_and_concatenate_pdfs(input_pdfs, page_numbers, output_pdf)
