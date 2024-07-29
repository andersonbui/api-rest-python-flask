
import requests

from app.services.apis_request.base_api_clients import BaseAPIClient

class CurrenciesInfoAPIClient(BaseAPIClient):
    """
        Summary:
        Cliente de API para obtener información de divisas.

        Explanation:
        Implementa el método para obtener información adicional de una divisa a través de una API externa. Utiliza el identificador de la divisa de un registro para realizar la solicitud a la API y devuelve un diccionario con la descripción de la divisa.

        Args:
        - record: El registro de datos que contiene el identificador de la divisa

        Returns:
        - Un diccionario con la descripción de la divisa obtenida de la API
        - En caso de error de conexión, puede lanzar una excepción ConnectionError
    """
    
    def fetch_additional_data(self, record):
        identifier = record.get('currency_id')
        if not identifier:
            return {}
        api_url = f"https://rocketchatdev.keos.co/currencies/{identifier}"
        response = requests.get(api_url, timeout=5)
        if (response.status_code == 502):
            raise ConnectionError(
                f"Api {api_url} no disponibles. status_code {response.status_code}"
            )
        return {
            "description": response.json().get('description'),
        }

