import requests
data = {"name" : "groceries1", 'shop':2}
r = requests.post('http://localhost:8000/Market/order/', json = data)
print(r.json)