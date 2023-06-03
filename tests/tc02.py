import requests, pprint

# 先登陆,获取sessionid
payload = {"username": "liubo", "password": "789456"}

response = requests.post("http://localhost/api/mgr/signin", data=payload)

retDict = response.json()
print(retDict)

sessionid = response.cookies["sessionid"]
print(sessionid)
# # 再发送列出请求，注意多了 pagenum 和 pagesize
# payload = {"action": "list_book", "pagenum": 8, "pagesize": 2}
#
# response = requests.get(
#     "http://localhost/api/mgr/books",
#     params=payload,
#     cookies={"sessionid": sessionid},
# )
#
# pprint.pprint(response.json())
