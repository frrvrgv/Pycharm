import requests
r = requests.get("https://videogamedb.uk:443/api/v2/videogame/2")
#fetch the json format of the response
print(r.json())
#text
print(r.text)
#status code
print(r.status_code)
#response url
print(r.url)
#request object
print(r.request)
#check the encoding of a response
print(r.encoding)
#close the connection
r.close()
#fetch the header
print(r.headers)
#response history
print(r.history)
