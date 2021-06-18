# Autenticacion Oauth - obtener access_token
import requests
import json

# First Step:
# Go to the github page
# developer github oauth -- registrar app github Oauth

client_secret = 'XXXXXXXXXXXXXXXXXXXX'
client_id = 'YYYYYYYYYYYYYYYYYYY'

ruta = 'https://github.com/login/oauth/authorize'
payload = {'client_id':client_id }#,'client_secret':client_secret}

respuesta = requests.get(ruta,payload)
print(respuesta.status_code)
print(respuesta.url)

code = input('Please input the code from url: ')
#https://github.com/login?client_id=bf186ec51be5654b29df&return_to=%2Flogin%2Foauth%2Fauthorize%3Fclient_id%3Dbf186ec51be5654b29df%26client_secret%3D1035d0e424c9828e39d6b19f92a5ec82e3ea21c0
#Abrimos la url en el navegador, autorizamos el uso de la app

#https://www.google.com.co/?code=a4eaffc3a260ec7fad1c
#code='34d1bc56494f45795d66'
# Obtenemos el code de la url a donde fuimos redirigidos luego de autorizar.

#2. Step!

payload = {'client_id':client_id,
           'client_secret':client_secret,
           'code':code}
headers = {'Accept':'application/json'}
ruta = 'https://github.com/login/oauth/access_token'


respuesta = (requests.post(ruta,payload,headers=headers))
print(respuesta.status_code)
print(respuesta.json())
respuesta_json = respuesta.json()
print(respuesta_json['access_token'])

# print(respuesta.text)
# respuesta =  json.loads(respuesta.text)
# print(type(respuesta))
# print(respuesta['access_token'])

