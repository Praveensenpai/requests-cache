from cache_request import cache_request

url = "https://api.ipify.org/?format=json"
params = None
headers = None


response = cache_request(url, params=params, headers=headers)

print(response.text)
