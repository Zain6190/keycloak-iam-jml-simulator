import requests

from config.settings import (
    KEYCLOAK_URL,
    ADMIN_REALM,
    ADMIN_CLIENT,
    ADMIN_USERNAME,
    ADMIN_PASSWORD,
)


class KeycloakAuth:
    """
    Handles authentication with Keycloak.
    Responsible only for obtaining the admin access token.
    """

    def __init__(self):
        self.access_token = None

    def login(self):
        url = f"{KEYCLOAK_URL}/realms/{ADMIN_REALM}/protocol/openid-connect/token"

        payload = {
            "client_id": ADMIN_CLIENT,
            "username": ADMIN_USERNAME,
            "password": ADMIN_PASSWORD,
            "grant_type": "password",
        }

        response = requests.post(url, data=payload)

        if response.status_code == 200:
            self.access_token = response.json()["access_token"]
            print("✅ Successfully authenticated with Keycloak.")
            return self.access_token

        raise Exception(
            f"Authentication Failed!\n"
            f"Status Code: {response.status_code}\n"
            f"{response.text}"
        )