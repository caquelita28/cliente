import requests


def obtener_respuesta_api():
    try:
        # Realizar la petición GET a la API
        respuesta = requests.get("https://192.168.1.16")

        # Verificar si la petición fue exitosa
        respuesta.raise_for_status()

        # Obtener y mostrar los datos en formato JSON
        datos = respuesta.json()
        print("Respuesta de la API:")
        print(f"Mensaje: {datos['mensaje']}")
        print(f"Estado: {datos['estado']}")

    except requests.exceptions.ConnectionError:
        print("Error: No se pudo conectar con la API. Asegúrate de que esté ejecutándose en http://localhost:8080")
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la petición: {e}")


if __name__ == '__main__':
    obtener_respuesta_api()