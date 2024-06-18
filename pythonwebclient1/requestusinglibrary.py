import json
import requests

data = {"name": "John Kennedy"}
r = requests.post('https://httpbin.org/post', json=data)
print(r.json())
