import requests, pprint
payload = { "pagenum": 1,"pagesize":5}
response = requests.get(
    "http://127.0.0.1/api/books/books",
    params=payload
)
pprint.pprint(response.json())
