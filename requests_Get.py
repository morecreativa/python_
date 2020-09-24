import requests

payload={
    'key1':'value',
    'key2':'value2',
    'key3':'value3',
}
r=requests.get('http://httpbin.org/get',params=payload)

print(list(payload.items()))
print('\n'+"______________next_____________"+'\n')
print(r.url)
print(r.text)
print(r.status_code)