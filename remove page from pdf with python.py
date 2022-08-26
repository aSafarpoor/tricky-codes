# from PyPDF2 import PdfFileMerger, PdfFileReader

# filename1 = 'nlp-lec-17.pdf' 
# filename2 = 'nlp-lec-18.pdf'

# merger = PdfFileMerger()

# merger.append(PdfFileReader(open(filename1, 'rb')))
# merger.append(PdfFileReader(open(filename2, 'rb')))




# merger.write("merged.pdf")

from PyPDF2 import PdfFileWriter, PdfFileReader

#page number is start from 0 :)
ptk1 = list(range(2,21))
ptk2 = list(range(19,29))


filename1 = 'nlp-lec-17.pdf' 
filename2 = 'nlp-lec-18.pdf'

infile1 = PdfFileReader(filename1, 'rb')
infile2 = PdfFileReader(filename2, 'rb')

output = PdfFileWriter()

for i in ptk1:
    p = infile1.getPage(i)
    output.addPage(p)

for i in ptk2:
    p = infile2.getPage(i)
    output.addPage(p)

with open('newfile.pdf', 'wb') as f:
    output.write(f)