import requests
from bs4 import BeautifulSoup
import time

# URL de la categoría Pokémon TCG
URL = "https://cddistribution.com/pe/categoria-producto/juguetes-nuevos/pokemon-tcg/"

# Headers para simular que somos un navegador real
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

vistos = set()

print("🔍 Bot iniciado, revisando CD Distribution…")

while True:
    try:
        respuesta = requests.get(URL, headers=HEADERS)
        respuesta.raise_for_status()  # Si falla la conexión, lanza error

        soup = BeautifulSoup(respuesta.text, "html.parser")

        # Buscar productos en la página
        productos = soup.find_all("h2", class_="woocommerce-loop-product__title")

        for p in productos:
            nombre = p.text.strip()
            if nombre not in vistos:
                print(f"🆕 Nuevo producto detectado: {nombre}")
                vistos.add(nombre)

    except Exception as e:
        print(f"❌ Error al conectar: {e}")

    time.sleep(30)  # Espera 30 segundos antes de revisar otra vez
