
#%%
import PyPDF2
pdfFileObj = open('../resources/purchase-orders/PO_300000001076033_PO2014545205_0.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)


# for page in range(0,pdfReader.numPages):
#   if page == 0:  
#     pageObj = pdfReader.getPage(page)
#     print(pageObj.extractText())
# %%
pageObj = pdfReader.getPage(0)
page1=pageObj.extractText()

pageObj = pdfReader.getPage(1)
page2=pageObj.extractText()

# %%
