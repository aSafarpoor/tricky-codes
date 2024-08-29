import fitz  # PyMuPDF
from PyPDF2 import PdfMerger, PdfReader
import os



def combine_pdfs_in_order(folder_path, file_suffixes, output_path):
    merger = PdfMerger()

    for x in range(1, 6):  # x ranges from 1 to 5
        for suffix in file_suffixes:
            pdf_filename = f"{x}{suffix}.pdf"
            pdf_path = os.path.join(folder_path, pdf_filename)

            if os.path.exists(pdf_path):
                merger.append(pdf_path)
            else:
                print(f"Warning: {pdf_filename} not found in the folder.")

    merger.write(output_path)
    merger.close()
    



def add_margins_and_resize(input_pdf_path, output_pdf_path,new_width,new_height):
    # Open the input PDF
    document = fitz.open(input_pdf_path)
    
    # Create the final output document
    output_document = fitz.open()
    
    # Iterate through pages
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        rect = page.rect
        
        
        
        # Create a new page with the increased size
        new_page = output_document.new_page(width=new_width, height=new_height)
        
        # Define the position to place the original page (top-right corner)
        new_rect = fitz.Rect(new_width - rect.width, 0, new_width, rect.height)
        
        # Insert the original page into the new page
        new_page.show_pdf_page(new_rect, document, page_num)
    
    # Save the output PDF
    output_document.save(output_pdf_path)
    output_document.close()
    document.close()
    
    print(f"PDF with added margins saved as {output_pdf_path}")



def print_page_sizes(pdf_path):
    reader = PdfReader(pdf_path)
    ws = []
    hs = []
    for i in range(len(reader.pages)):
        # page = reader.getPage(i)
        page = reader.pages[i]
        media_box = page.mediabox
        width = media_box.width
        height = media_box.height
        ws.append(width)
        hs.append(height)

    # print(max(ws),max(hs))
    return max(ws),max(hs)



#combine files
folder_path = os.getcwd()  # Use the current working directory
file_suffixes = ['1', '2', 's']
output_path = os.path.join(folder_path, "out1.pdf")
combine_pdfs_in_order(folder_path, file_suffixes, output_path)

#find suitable size
output_pdf_path = "out1.pdf"
maxws,maxhs = print_page_sizes(output_pdf_path)

#change size to suitable one
input_pdf_path = "out1.pdf"
output_pdf_path = "final.pdf"
add_margins_and_resize(input_pdf_path, output_pdf_path,new_width =int(maxws)+1,new_height= int(maxhs)+1)

os.remove("out1.pdf")