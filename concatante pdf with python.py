'''
In new version of PyPDF2:
There is PdfMerger, PdfReader instead of PdfFileMerger, PdfFileReader
'''

# from PyPDF2 import PdfFileMerger, PdfFileReader

# filename1 = 'nlp-lec-07.pdf' 
# filename2 = 'nlp-lec-08.pdf'
# filename3 = 'nlp-lec-09-10.pdf'
# filename4 = 'nlp-lec-11-12.pdf'

# merger = PdfFileMerger()

# merger.append(PdfFileReader(open(filename1, 'rb')))
# merger.append(PdfFileReader(open(filename2, 'rb')))
# merger.append(PdfFileReader(open(filename3, 'rb')))
# merger.append(PdfFileReader(open(filename4, 'rb')))


# merger.write("merged.pdf")

from PyPDF2 import PdfFileMerger, PdfFileReader
from tqdm import tqdm

merger = PdfFileMerger()
for i in tqdm(range(1,29+1)):
    if i == 29:
        merger.write("mr_mohammadi_DIP.pdf")
        break
    elif i<10:
        filename = 'session_'+ '0' + str(i) + '.pdf'
    else:
        filename = 'session_'+  str(i) + '.pdf'
    merger.append(PdfFileReader(open(filename, 'rb')))
