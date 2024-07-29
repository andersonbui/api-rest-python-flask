
import requests

from app.services.apis_request.base_api_clients import BaseAPIClient

class CurrenciesInfoAPIClient(BaseAPIClient):
    
    def fetch_additional_data(self, record):
        identifier = record.get('currency_id')
        if not identifier:
            return {}
        api_url = f"https://rocketchatdev.keos.co/currencies/{identifier}"
        response = requests.get(api_url)
        return {
            "description": response.json().get('description'),
        }

