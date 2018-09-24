import requests
data = {"name" : "frozen", 'product':2, 'order':2}
r = requests.post('http://localhost:8000/Market/line/', json = data)
print(r.json)