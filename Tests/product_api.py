import requests
data = {"name" : "Car", 'shop':2, 'value':100}
r = requests.post('http://localhost:8000/Market/product/', json = data)
print(r.json)