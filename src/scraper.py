import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

def contar_y_guardar_noticias(url, html_content=None):
    """
    Rastrea la página de BBC Mundo, cuenta las noticias usando un selector
    específico basado en el HTML proporcionado y guarda el resultado en noticias.jsonl.
    """
    if html_content is None:
        try:
            # 1. Realizar la solicitud HTTP (si no se proporciona el contenido)
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            response = requests.get(url, headers=headers)
            response.raise_for_status() # Lanza un error para códigos de estado 4xx/5xx
            html_content = response.content
        except requests.exceptions.RequestException as e:
            print(f"❌ Error al intentar conectar o descargar la página: {e}")
            return
            
    # 2. Analizar el contenido HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # 3. Detectar las noticias
    # Selector basado en el HTML proporcionado: buscar todos los <li> dentro del <ul> con el atributo data-testid="topic-promos".
    # Este es el contenedor de la sección "Principales".
    selector_noticias = 'ul[data-testid="topic-promos"] > li'
    noticias_elements = soup.select(selector_noticias)

    # Contar las noticias
    num_noticias = len(noticias_elements)

    # 4. Preparar el dato para JSONL
    data = {
        "fecha_extraccion": datetime.now().isoformat(),
        "url_origen": url,
        "total_noticias_detectadas": num_noticias,
        "selector_css_usado": selector_noticias
    }

    # 5. Generar el archivo noticias.jsonl (en modo 'a' para añadir la línea)
    nombre_archivo = "noticias.jsonl"
    try:
        with open(nombre_archivo, 'a', encoding='utf-8') as f:
            # Escribir el objeto JSON seguido de un salto de línea
            f.write(json.dumps(data, ensure_ascii=False) + '\n')
    except Exception as e:
        print(f"❌ Error al escribir en el archivo {nombre_archivo}: {e}")
        return

    print(f"✅ Proceso completado exitosamente.")
    print(f"   Se detectaron {num_noticias} noticias en la sección 'Principales'.")
    print(f"   Datos añadidos al archivo '{nombre_archivo}'.")


# URL objetivo
URL_BBC_MUNDO = "https://www.bbc.com/mundo"