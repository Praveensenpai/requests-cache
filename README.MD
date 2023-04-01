## Request Caching with Python Requests-Cache

This is a Python module that demonstrates how to implement request caching using the `requests-cache` package. This technique can be useful for applications that rely heavily on HTTP requests and APIs, as it can help reduce server load and improve response time by caching the results of previous requests.

### Installation

The `requests-cache` and `rich` package can be installed using pip:

Copy code

`pip install requests-cache rich`

### Usage

This module contains a function `cache_request` that sends a GET request to a specified URL using a cached session. Here's how to use it:

pythonCopy code

`from cache_request import cache_request  url = "https://api.ipify.org/?format=json" params = None headers = None  response = cache_request(url, params=params, headers=headers)  print(response.json())`

When you run this code for the first time, it will send a request to the specified URL and cache the response. On subsequent runs, the cached response will be returned instead of sending a new request.

The cached session is initialized with an expiration time of 24 hours, which can be modified by changing the `expire_after` parameter in the `CachedSession` constructor.

### Output

The `cache_request` function prints some information about the response, including the request URL, whether the response was returned from the cache, when the response was created, when it will expire, and whether it has already expired.

pythonCopy code

`URL: https://api.ipify.org/?format=json Response cache status: False Response created at: 2023-04-01T12:00:00.000000Z Response expiration time: 2023-04-02T12:00:00.000000Z Is response expired? False`
