import http.client
import circuitbreaker
@circuitbreaker.circuit
def make_request():
    conn = http.client.HTTPSConnection("https://videogamedb.uk:443")
    conn.request("GET", "/api/videogame/")
    response = conn.getresponse()
    conn.close()
    if response.status ==200:
        print("request successfull")
    else:
        raise Exception("Request failed with status code:",response.status)
try:
    result = make_request()
    print(result)
except circuitbreaker.CircuitBreakerError as e:
    print("Circuit breaker is open request not send")