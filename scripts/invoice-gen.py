"""
import PyPDF2
pdfFileObj = open('./resources/purchase-orders/PO_300000001076033_PO2014545205_0.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)

'''
for page in range(0,pdfReader.numPages):
    pageObj = pdfReader.getPage(page)
    print(pageObj.extractText())
'''

pageObj = pdfReader.getPage(0)
print(pageObj.extractText())

'''
print(str(pdfReader.getFields))

"""
import sys
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdftypes import resolve1

#filename = sys.argv[1]
filename='../resources/purchase-orders/PO_300000001076033_PO2014545204_0.pdf'
fp = open(filename, 'rb')

parser = PDFParser(fp)
doc = PDFDocument(parser)

print(str(doc))

fields = resolve1(doc.catalog['AcroForm'])['Fields']
# for i in fields:
#     field = resolve1(i)
#     name, value = field.get('T'), field.get('V')
#     print('{0}: {1}'.format(name, value))
