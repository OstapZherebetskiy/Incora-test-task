
import requests
import json

def Js(r):
    my_json = r.content.decode('utf8').replace("'", '"')


    # Load the JSON to a Python list & dump it back out as formatted JSON
    data = json.loads(my_json)
    s = json.dumps(data, indent=4, sort_keys=True)
    print(s)
    print('-'* 50)


# r = requests.post('http://127.0.0.1:8000/accounts/user/', data={
#     'email': 'tarsssst@gmail.com', 
#     'password': '123qaz123', 
#     'password2': '123qaz123', 
#     'first_name': 'osadap',
#     'phone_number': '12345678'
#     })
# print(r.content)



# r = requests.post('http://127.0.0.1:8000/accounts/login', data={
#     'email': 'tarst@gmail.com', 
#     'password': '123qaz123', 
    
#     })
# print(r.content)



token = 'Bearer ' + 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU2NDQ1MDY1LCJpYXQiOjE2NTY0NDQ3NjUsImp0aSI6IjAwYjBmMjc0OGUxMTRjYWVhNjMwZWQ2MmYwNmM1ZjhkIiwidXNlcl9pZCI6M30.Q7O6W9kko7Y_nIM6Uo1L36fI0pmMjFC8ezD5bJ4DS9Q'

user = requests.put('http://127.0.0.1:8000/accounts/user/1/', params={'phone_number': '12345678'})
print('-' * 20)

print(user.content)
# Js(user)









