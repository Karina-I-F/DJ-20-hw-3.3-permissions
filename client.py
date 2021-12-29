import requests

HOST = 'http://127.0.0.1:8000/api/v1/'

#  get urls
resp = requests.get(f'{HOST}').json()
print(resp)

# get all advertisements
resp = requests.get(f'{HOST}advertisements/').json()
print(resp)

# filtering by author
resp = requests.get(f'{HOST}advertisements/?creator=3').json()
print(resp)

# filtering by date
resp = requests.get(f'{HOST}advertisements/?created_at_before=2021-12-28').json()
print(resp)

# filtering by status
resp = requests.get(f'{HOST}advertisements/?status=OPEN').json()
print(resp)

# create advertisement 1
resp = requests.post(f'{HOST}advertisements/',
                     json={
                         "title": "Шкаф IKEA",
                         "description": "Срочно"},
                     headers={
                         "Authorization": "Token put_your_token_here"
                     }).json()
print(resp)

# create advertisement 2
resp = requests.post(f'{HOST}advertisements/',
                     json={
                         "title": "Клубника",
                         "description": "Сочная и спелая"},
                     headers={
                         "Authorization": "Token put_your_token_here"
                     }).json()
print(resp)

# update advertisement
resp = requests.patch(f'{HOST}advertisements/1/',
                      json={
                            "status": "CLOSED"},
                      headers={
                         "Authorization": "Token put_your_token_here"
                      }).json()
print(resp)

# delete advertisement
resp = requests.delete(f'{HOST}advertisements/2/',
                       headers={
                           "Authorization": "Token put_your_token_here"
                       })
print(resp.status_code)

