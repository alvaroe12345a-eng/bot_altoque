import os
os.environ['PORT'] = '10000'
import requests
import time
from twilio.rest import Client

account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
twilio_number = os.environ.get('TWILIO_NUMBER')
my_number = os.environ.get('MY_NUMBER')
url = 'https://www.ejemplo.com/pagina'

archivo_guardado = 'contenido_anterior.txt'

if os.path.exists(archivo_guardado):
    with open(archivo_guardado, 'r', encoding='utf-8') as f:
        ultimo_contenido = f.read()
else:
    ultimo_contenido = requests.get(url).text
    with open(archivo_guardado, 'w', encoding='utf-8') as f:
        f.write(ultimo_contenido)

client = Client(account_sid, auth_token)

while True:
    try:
        respuesta = requests.get(url)
        if respuesta.text != ultimo_contenido:
            client.messages.create(
                body="¡Hola! Se ha agregado un nuevo artículo en la página. Revisa aquí: " + url,
                from_=twilio_number,
                to=my_number
            )
            ultimo_contenido = respuesta.text
            with open(archivo_guardado, 'w', encoding='utf-8') as f:
                f.write(ultimo_contenido)
        time.sleep(60)
    except Exception as e:
        print("Error:", e)
        time.sleep(60)
