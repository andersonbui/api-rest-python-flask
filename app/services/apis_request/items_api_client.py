
import requests

from app.services.apis_request.base_api_clients import BaseAPIClient


class ItemsInfoAPIClient(BaseAPIClient):
    """
        Summary:
        Cliente de API para obtener información de artículos.

        Explanation:
        Implementa el método para obtener información adicional de un artículo a través de una API externa. Utiliza el identificador único del artículo para realizar la solicitud a la API y devuelve un diccionario con varios detalles del artículo.

        Args:
        - record: El registro de datos que contiene información relacionada con el artículo

        Returns:
        - Un diccionario con el precio, fecha de creación, identificador de categoría, identificador de divisa y otros detalles del artículo obtenidos de la API
        - En caso de error de conexión, puede lanzar una excepción ConnectionError
    """
    
    def fetch_additional_data(self, record):
        identifier = record.get('site') + record.get('id')
        api_url = f"https://rocketchatdev.keos.co/items/{identifier}"
        response = requests.get(api_url, timeout=5)
        if (response.status_code == 502):
            raise ConnectionError(
                f"Api {api_url} no disponibles. status_code {response.status_code}"
            )
        return {
            "price": response.json().get('price'),
            "start_time": response.json().get('date_created'),
            "category_id": response.json().get('category_id'),
            "currency_id": response.json().get('currency_id'),
            "seller_id": response.json().get('seller_id'),
        }
