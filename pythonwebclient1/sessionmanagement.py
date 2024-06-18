import requests
url = 'https://jsonplaceholder.typicode.com/posts'
session = requests.Session()
response = session.get(url)
print(response.json())
response = session.post(url,json={"title": "new post", "body":"content"})
print(response.json())
session.close()