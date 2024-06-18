import requests
url = 'https://api.github.com/search/repositories,params={"q":"language":"python","sort":"stars","order":"desc"}'
response = requests.get(url)
json_response = response.json()
print(json_response)