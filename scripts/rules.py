def insert_sequence(str1, str2, int):
    """ (str1, str2, int) -> str

    Return the DNA sequence obtained by inserting the 
    second DNA sequence into the first DNA sequence 
    at the given index.

    >>> insert_sequence('CCGG', 'AT', 2)
    CCATGG
    >>> insert_sequence('CCGG', 'AT', 3)
    CCGATG
    >>> insert_sequence('CCGG', 'AT', 4)
    CCGGAT
    >>> insert_sequence('CCGG', 'AT', 0)
    ATCCGG
    >>> insert_sequence('CCGGAATTGG', 'AT', 6)
    CCGGAAATTTGG

    """

    str1_split1 = str1[:int]
    str1_split2 = str1[int:]
    new_string = str1_split1 + str2 + str1_split2
    return new_string


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
# text=insert_sequence(text,'\t',text.find('Item',0))
# text=insert_sequence(text,'\t',text.find('Price',0))
# text=insert_sequence(text,'\t',text.find('Quantity',0))
# text=insert_sequence(text,'\t',text.find('UOM',0))
# text=insert_sequence(text,'\t',text.find('Ordered',0))
# text=insert_sequence(text,'\t',text.find('Taxable',0))
# text=insert_sequence(text,'\t',text.find('Taxable')+7)
# text=insert_sequence(text,'\t',text.find('Taxable\t')+9)
