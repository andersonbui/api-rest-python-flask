
import requests

from app.services.apis_request.base_api_clients import BaseAPIClient

class UsersInfoAPIClient(BaseAPIClient):
    """
        Summary:
        Cliente de API para obtener información de usuarios.

        Explanation:
        Implementa el método para obtener información adicional de un usuario a través de una API externa. Utiliza el identificador de vendedor del usuario para realizar la solicitud a la API y devuelve un diccionario con el apodo del usuario.

        Args:
        - record: El registro de datos que contiene el identificador del vendedor (seller_id) del usuario

        Returns:
        - Un diccionario con el apodo del usuario obtenido de la API
        - En caso de error de conexión, puede lanzar una excepción ConnectionError
    """
    
    def fetch_additional_data(self, record):
        identifier = record.get('seller_id')
        if not identifier:
            return {}
        api_url = f"https://rocketchatdev.keos.co/users/{identifier}"
        response = requests.get(api_url, timeout=5)
        if (response.status_code == 502):
            raise ConnectionError(
                f"Api {api_url} no disponibles. status_code {response.status_code}"
            )
        return {
            "nickname": response.json().get('nickname'),
        }

