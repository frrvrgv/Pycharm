import requests
r = requests.delete('https://videogamedb.uk:443/api/v2/videogame/2')
print(r)
print(r.text)