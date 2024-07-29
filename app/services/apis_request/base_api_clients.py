
class BaseAPIClient:
    def fetch_additional_data(self, record):
        raise NotImplementedError("Subclasses must implement fetch_additional_data method.")
