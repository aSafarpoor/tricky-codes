import os
import PyPDF2

def remove_non_alphabetic(text):
    """
    Remove non-alphabetic characters from the input text, keeping spaces.

    Parameters:
    - text (str): The input text.

    Returns:
    - str: The text with only alphabetic characters and spaces.
    """
    alphabetic_text = ''.join(char for char in text if char.isalpha() or char.isspace())
    return alphabetic_text



def get_pdf_title(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            title = pdf_reader.metadata.title
            print(title)
            return remove_non_alphabetic(title)
    except Exception as e:
        print(f"Error reading title from {pdf_path}: {e}")
        return None

def rename_pdf_with_title(pdf_path):
    title = get_pdf_title(pdf_path)
    if title:
        pdf_dir, pdf_filename = os.path.split(pdf_path)
        new_filename = f"{title}.pdf"
        new_path = os.path.join(pdf_dir, new_filename)

        try:
            os.rename(pdf_path, new_path)
            print(f"Renamed: {pdf_filename} -> {new_filename}")
        except Exception as e:
            print(f"Error renaming {pdf_filename}: {e}")

def batch_rename_pdfs(pdf_folder):
    for root, dirs, files in os.walk(pdf_folder):
        for file in files:
            if file.lower().endswith('.pdf'):
                pdf_path = os.path.join(root, file)
                rename_pdf_with_title(pdf_path)

# Example usage:
pdf_folder_path = './'
batch_rename_pdfs(pdf_folder_path)
