
from invoice2data import extract_data
result = extract_data('./resources/purchase-orders/PO_300000001076033_PO2014545205_0.pdf')
print(result)

"""
veryfi_client = Client(client_id, client_secret, username, api_key)
categories = ['Grocery', 'Utilities', 'Travel'] # list of your categories
file_path = '../resources/purchase-orders/invoice.jpg'
response = veryfi_client.process_document(file_path, categories=categories)
print (response)
"""