import requests
import json
#import pprint
# First Step:
# Go to the github page
# developer github oauth -- registrar app github Oauth

client_secret = '1035d0e424c9828e39d6b19f92a5ec82e3ea21c0'
client_id = 'bf186ec51be5654b29df'

access_token = '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'
access_token_modifiy = 'token ' + access_token
headers = {'Authorization':access_token_modifiy}


# Consultar repositorios
ruta = 'https://api.github.com/user/repos'

response = requests.get(ruta,headers=headers)
print(response.status_code)
#archivo-salida.py
f = open ('archivo.json','w')
f.write(response.text)
f.close()

response = response.json()
#print(dir(response))
#print(response.content)
#print(response.text)
print(type(response))
for project in response:
    print(project['name'])


