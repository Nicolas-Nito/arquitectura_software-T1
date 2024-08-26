import requests
import time

def query_api():
	url = "http://fastapi:8000/"  # Reemplaza con tu endpoint de FastAPI
	try:
		response = requests.get(url)
		if response.status_code == 200:
			print("Respuesta de la API:", response.json())
		else:
			print(f"Error en la consulta: {response.status_code}")
	except requests.exceptions.RequestException as e:
		print(f"Error al conectar con la API: {e}")

if __name__ == "__main__":
	while True:
		query_api()
		time.sleep(10)