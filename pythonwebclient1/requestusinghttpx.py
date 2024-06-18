import httpx


data = {"name": "John Kennedy"}
r = httpx.post('https://httpbin.org/post', json=data)
print(r.json())