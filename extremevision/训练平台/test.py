import  requests

import sys
import hashlib
import os


file_name = r"C:\Users\Administrator\Desktop\实例代码\hc\1.jpg"



url = "https://test.cvmart.net/api/file/max-file/upload"
headers = {
'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36', 'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9lYWdsZS1uZXN0LWJhY2tlbmQtc2VydmljZS5kZXZsb3Auc3ZjLmNsdXN0ZXIubG9jYWxcL2FwaVwvbG9naW4iLCJpYXQiOjE1ODk2MTA3MDAsImV4cCI6MTU4OTYxNzkwMCwibmJmIjoxNTg5NjEwNzAwLCJqdGkiOiJ0c0lMZXJ4Z2JuQlMxV05mIiwic3ViIjoxMjA3LCJwcnYiOiIyM2JkNWM4OTQ5ZjYwMGFkYjM5ZTcwMWM0MDA4NzJkYjdhNTk3NmY3In0.O9v3LCTOPTPxXyXYjaSITOQ28tVZuuIIQykuigcGAAw'}
with open(file_name,"rb") as f:
    a1 = f.read()

with open(file_name, 'rb') as fp:
    data = fp.read()
    file_md5= hashlib.md5(data).hexdigest()
    print(file_md5)
    data = {
        "chunk_data":a1,
        "hash":file_md5,
        "current_hash":file_md5,
        "filename":"1.jpg",
        "size":os.path.getsize(file_name),
        "current_chunk":1,
        "total_chunk":1
    }

    a1 = requests.post(url,data=data,headers=headers)
    print(a1.json())