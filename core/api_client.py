import requests

from config.settings import KEYCLOAK_URL


class KeycloakAPI:

    def __init__(self, token):

        self.base_url = KEYCLOAK_URL

        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }

    # ---------------- GET ----------------

    def get(self, endpoint):

        url = self.base_url + endpoint

        response = requests.get(
            url,
            headers=self.headers
        )

        return response

    # ---------------- POST ----------------

    def post(self, endpoint, data):

        url = self.base_url + endpoint

        response = requests.post(
            url,
            headers=self.headers,
            json=data
        )

        return response

    # ---------------- PUT ----------------

    def put(self, endpoint, data=None):

        url = self.base_url + endpoint

        response = requests.put(
            url,
            headers=self.headers,
            json=data
        )

        return response

    # ---------------- DELETE ----------------

    def delete(self, endpoint):

        url = self.base_url + endpoint

        response = requests.delete(
            url,
            headers=self.headers
        )

        return response