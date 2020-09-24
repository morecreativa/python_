import requests
import json

url='https://swapi.dev/api'
uri=url+'/people/1/'

data=requests.get(uri).json()

print(data)
print('\n'+"______________next_____________"+'\n')
print(data['name'],data['height'])
