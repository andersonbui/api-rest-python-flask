
import requests

from app.services.apis_request.base_api_clients import BaseAPIClient

class UsersInfoAPIClient(BaseAPIClient):
    
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

