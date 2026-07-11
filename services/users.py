from config.settings import REALM


class UserService:

    def __init__(self, api):
        self.api = api

    # ----------------------------
    # List All Users
    # ----------------------------
    def get_all_users(self):

        response = self.api.get(f"/admin/realms/{REALM}/users")

        if response.status_code == 200:
            return response.json()

        return []

    # ----------------------------
    # Get User By ID
    # ----------------------------
    def get_user(self, user_id):

        response = self.api.get(
            f"/admin/realms/{REALM}/users/{user_id}"
        )

        if response.status_code == 200:
            return response.json()

        return None

    # ----------------------------
    # Create User (JOINER)
    # ----------------------------
    def create_user(self, username, email, password):

        payload = {
            "username": username,
            "email": email,
            "enabled": True,
            "emailVerified": True,
            "credentials": [
                {
                    "type": "password",
                    "value": password,
                    "temporary": False
                }
            ]
        }

        response = self.api.post(
            f"/admin/realms/{REALM}/users",
            payload
        )

        return response