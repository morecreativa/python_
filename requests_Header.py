import requests

url = 'https://httpbin.org/get'

r=requests.get(url)

print(r.text)
print('\n'+"______________next_____________"+'\n')

# you can change youre Response Body
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)

print(r.status_code)
print(r.headers)
print('\n'+"______________next_____________"+'\n')
print(r.text)