import http.client
import socket
try:
    conn = http.client.HTTPSConnection("https://videogamedb.uk:443")
    conn.request("GET" ,"/api/videogame/")
    response = conn.getresponse()
except(http.client.HTTPException, socket.error) as e:
    print("Network or http error",e)
finally:
    conn.close()