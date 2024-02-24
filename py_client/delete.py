import requests

product_id = input("Enter your product ID want delete: ")

try:
    product_id = int(product_id)
except: 
    product_id = None
    print(f'{product_id} not a valid id')
    
if product_id:
    endpoints = f"http://127.0.0.1:8000/api/products/{product_id}/delete/"
    get_response = requests.delete(endpoints)
    print(get_response.status_code, get_response.status_code==204)
    