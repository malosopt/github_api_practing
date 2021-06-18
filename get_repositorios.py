import requests
import json

# First Step:
# Go to the github page
# developer github oauth -- registrar app github Oauth

client_secret = 'XXXXXXXXXXXXXXXXXXXXXXX'
client_id = 'YYYYYYYYYYYYYYYYYYYY'
access_token = 'ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ'

# CURL instruccion
#$ curl -H "Authorization: token OAUTH-TOKEN" https://api.github.com/user/repos
access_token_modifiy = 'token ' + access_token
headers = {'Authorization':access_token_modifiy}
# pasas access_token por headers

# Consultar repositorios
ruta = 'https://api.github.com/user/repos'

response = requests.get(ruta,headers=headers)
print(f'status: {response.status_code}')

#archivo-salida.py
f = open ('archivo.json','w') #w write
f.write(response.text)
f.close()

response = response.json()
# print(dir(response))
# print(response.content)
# print(response.text)
# print(type(response))
for project in response:
    print('------------------')
    print(project['name'])


