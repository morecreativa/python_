import requests

r=requests.get('https://httpbin.org/get')
print(r.text)
print('\n'+"______________next_____________"+'\n')
r=requests.post('https://httpbin.org/post',data={'key':'value'})

# text stream Response body
print(r.text) 
print('\n'+"______________next_____________"+'\n')

# status_code print Status
print(r.status_code)
print('\n'+"______________next_____________"+'\n')

# header response just Response Headers!!!!!
print(r.headers)
