from core.auth import KeycloakAuth
from core.api_client import KeycloakAPI
from core.logger import AuditLogger
from services.users import UserService


def main():

    print("=" * 50)
    print("KEYCLOAK JML SIMULATOR")
    print("=" * 50)

    # Login
    auth = KeycloakAuth()
    token = auth.login()

    AuditLogger.login("admin")

    # API Client
    api = KeycloakAPI(token)

    # User Service
    users_service = UserService(api)

    while True:

        print("\n" + "=" * 50)
        print("        KEYCLOAK IAM CONSOLE")
        print("=" * 50)

        print("1. List Users")
        print("2. Create User")
        print("3. Search User")
        print("4. Disable User")
        print("5. Delete User")
        print("6. Exit")

        choice = input("\nSelect Option: ")

        # ===========================
        # LIST USERS
        # ===========================
        if choice == "1":

            users = users_service.get_all_users()

            print(f"\nTotal Users : {len(users)}\n")

            for user in users:

                print("----------------------------")
                print("Username :", user.get("username"))
                print("Email    :", user.get("email"))
                print("Enabled  :", user.get("enabled"))

        # ===========================
        # CREATE USER
        # ===========================
        elif choice == "2":

            print("\nCreate New User")
            print("-" * 30)

            username = input("Username : ")
            email = input("Email    : ")
            password = input("Password : ")

            response = users_service.create_user(
                username,
                email,
                password
            )

            if response.status_code == 201:

                AuditLogger.create_user(username)

                print("\n✅ User Created Successfully!")

            else:

                print("\n❌ Failed to Create User")

                print("Status :", response.status_code)

                print(response.text)

        # ===========================
        # EXIT
        # ===========================
        elif choice == "6":

            print("\nGood Bye!\n")

            break

        # ===========================
        # OTHER OPTIONS
        # ===========================
        else:

            print("\n🚧 Feature Coming Soon...\n")


if __name__ == "__main__":
    main()