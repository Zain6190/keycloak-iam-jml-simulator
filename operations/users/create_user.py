from services.users import UserService
from core.logger import AuditLogger


class CreateUserOperation:

    def __init__(self, api):

        self.users = UserService(api)

    def execute(self):

        print("\nCreate New User")
        print("-" * 30)

        username = input("Username : ")
        email = input("Email    : ")
        password = input("Password : ")

        response = self.users.create_user(
            username,
            email,
            password
        )

        if response.status_code == 201:

            print("\n✅ User Created Successfully.")

            AuditLogger.info(
                f"Created user '{username}'"
            )

        else:

            print("\n❌ Failed to create user.")
            print(response.text)