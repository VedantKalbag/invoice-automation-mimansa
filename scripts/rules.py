COUNTRY_NAME_LENGTH=5

"""
def insert_sequence(str1, str2, int):
    str1_split1 = str1[:int]
    str1_split2 = str1[int:]
    new_string = str1_split1 + str2 + str1_split2
    return new_string
"""

poNumber=page1[page1.find('Page')+4:page1.find('Business')]
businessUnit=page1[page1.find('Unit')+4:page1.find('Send')]
contactName=page1[page1.find('Contact')+7:page1.find('E-mail')-1]
contactEmail=page1[page1.find('E-mail ')+7:page1.find('.com')+4]
invoiceHardcopyAddress=page1[page1.find('.com')+4:page1.find('Buyer')]
clientGSTN=page1[page1.find('(GST/QST/HST)')+14:page1.find('Supplier')]
billDate=page2[page2.find('Ordered Date')+12 : page2.find('SupplierAddress')]
billToAddress=page2[page2.find('Bill To Address')+15: page2.find('Ship To Address')-1]
shipToAddress=page2[page2.find('Ship To Address')+15: page2.find('For Invoice Payment')]
secondEmail=page2[page2.find('QueriesEmail: ')+14 : page2.find('.com')+4]

#Processing Itemized List
text=page2[page2.find('LineItemPriceQuantity') : -1]
"""
# text=insert_sequence(text,'\t',text.find('Item',0))
# text=insert_sequence(text,'\t',text.find('Price',0))
# text=insert_sequence(text,'\t',text.find('Quantity',0))
# text=insert_sequence(text,'\t',text.find('UOM',0))
# text=insert_sequence(text,'\t',text.find('Ordered',0))
# text=insert_sequence(text,'\t',text.find('Taxable',0))
# text=insert_sequence(text,'\t',text.find('Taxable')+7)
# text=insert_sequence(text,'\t',text.find('Taxable\t')+9)
"""

val=float(text[text.find(',')-1:text.find('.00')+3].replace(',',''))
total=float(text[text.find('Total',text.find('Line Total')+10)+5:-1].replace(',',''))
qty=float(text[text.find('Promised')+8:text.find('Each',text.find('Promised'))])

if qty*val==total:
    itemQty=qty
    itemVal=val
    invoiceTotal=total
else:
    val=float(text[text.find(',')-2:text.find('.00')+3].replace(',',''))
    total=float(text[text.find('Total',text.find('Line Total')+10)+5:-1].replace(',',''))
    qty=float(text[text.find('Promised')+8:text.find('Each',text.find('Promised'))])

itemDescription = text[text.find('Taxable')+8 : text.find(',')-1]

temp=billToAddress[::-1]
for x in temp:
    if x.isdigit():
        index = temp.index(x)
        break
state=billToAddress[-index:]
state=state[:len(state)-COUNTRY_NAME_LENGTH]

