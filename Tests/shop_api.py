import requests
data = {"name" : "hello"}
r = requests.post('http://localhost:8000/Market/shop/', json = data)
print(r.json)