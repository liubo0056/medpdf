import json
import requests,pprint
"""登录测试"""
# payload = {
#     'username': 'liubo',
#     'password': '789456'
# }
# response = requests.post('http://localhost/api/common/signin',
#               data=payload)
# pprint.pprint(response.json())

"""登出测试"""
# response = requests.post('http://localhost/api/common/signout')
# pprint.pprint(response.json())

"""图书查血测试"""
res = requests.get('http://localhost/api/books/books')
res_data = res.content.decode('utf-8')
books = json.loads(res_data)
print(books)

