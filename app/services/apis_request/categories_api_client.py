
import requests

from app.services.apis_request.base_api_clients import BaseAPIClient

class CategoryInfoAPIClient(BaseAPIClient):
    
    def fetch_additional_data(self, record):
        identifier = record.get('category_id')
        if not identifier:
            return {}
        api_url = f"https://rocketchatdev.keos.co/categories/{identifier}"
        response = requests.get(api_url)
        return {
            "name": response.json().get('name'),
        }

