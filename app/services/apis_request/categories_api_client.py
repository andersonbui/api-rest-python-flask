
import requests

from app.services.apis_request.base_api_clients import BaseAPIClient

class CategoryInfoAPIClient(BaseAPIClient):
    """
        Summary:
        Cliente de API para obtener información de categorías.

        Explanation:
        Implementa el método para obtener información adicional de una categoría a través de una API externa. Utiliza el identificador de categoría de un registro para realizar la solicitud a la API y devuelve un diccionario con el nombre de la categoría.

        Args:
        - record: El registro de datos que contiene el identificador de la categoría

        Returns:
        - Un diccionario con el nombre de la categoría obtenido de la API
        - En caso de error de conexión, puede lanzar una excepción ConnectionError
    """
    
    def fetch_additional_data(self, record):
        identifier = record.get('category_id')
        if not identifier:
            return {}
        api_url = f"https://rocketchatdev.keos.co/categories/{identifier}"
        response = requests.get(api_url, timeout=5)
        if (response.status_code == 502):
            raise ConnectionError(
                f"Api {api_url} no disponibles. status_code {response.status_code}"
            )
        return {
            "name": response.json().get('name'),
        }

