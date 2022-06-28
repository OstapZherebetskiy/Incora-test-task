
import requests
import json


def Js(r):
    my_json = r.content.decode('utf8').replace("'", '"')


    # Load the JSON to a Python list & dump it back out as formatted JSON
    data = json.loads(my_json)
    s = json.dumps(data, indent=4, sort_keys=True)
    print(s)


URL = 'http://127.0.0.1:8000/log/login/'

client = requests.session()

# Retrieve the CSRF token first
client.get(URL)  # sets cookie
if 'csrftoken' in client.cookies:
    # Django 1.6 and up
    csrftoken = client.cookies['csrftoken']
else:
    # older versions
    csrftoken = client.cookies['csrf']

login_data = dict(username='ostap', password='12345', csrfmiddlewaretoken=csrftoken)
# print(login_data)
r = client.post(URL, data=login_data, headers=dict(Referer=URL))
Js(r)



log = client.get('http://127.0.0.1:8000/api/post/')



# log = client.post('http://127.0.0.1:8000/api/post/', data={'title': 'bbbb', 'body': 'aabbbbbaaa'}, headers={"X-CSRFToken": csrftoken})
# Js(log)
# print(log.headers)




