from PyPDF2 import PdfFileWriter, PdfFileReader

ptk1 = list(range(1,11))

filename1 = 'Are Graph Augmentations Necessary Simple Graph Contrastive Learning for Recommendation.pdf' 

infile1 = PdfFileReader(filename1, 'rb')

output = PdfFileWriter()

for i in ptk1:
    p = infile1.getPage(i)
    output.addPage(p)

with open('newfile.pdf', 'wb') as f:
    output.write(f)
