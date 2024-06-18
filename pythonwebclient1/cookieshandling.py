import http.client
import http.cookiejar

#create a cookie_jar to store the cookie
cookie_jar = http.cookiejar.CookieJar()

#create a http connection with cookie support
conn = http.client.HTTPSConnection("http://videogamedb.uk,Set-Cookie = cookie_jar")
conn.request("GET", "/")
response = conn.getresponse()
