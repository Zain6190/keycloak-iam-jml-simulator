from services.users import UserService
from core.logger import AuditLogger


class SearchUserOperation:

    def __init__(self, api):

        self.users = UserService(api)

    def execute(self):

        username = input("\nEnter Username : ")

        users = self.users.search_user(username)

        if len(users) == 0:

            print("\n❌ User not found.")

            return

        print("\nUser Found\n")

        for user in users:

            print("----------------------------")
            print("ID       :", user.get("id"))
            print("Username :", user.get("username"))
            print("Email    :", user.get("email"))
            print("Enabled  :", user.get("enabled"))

        AuditLogger.info(
            f"Searched user '{username}'"
        )