from core.auth import KeycloakAuth
from core.api_client import KeycloakAPI
from core.logger import AuditLogger
from services.users import UserService


def main():

    print("=" * 50)
    print("KEYCLOAK IAM SIMULATOR")
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
        print("4. Update User")
        print("5. Disable User")
        print("6. Delete User")
        print("7. Exit")

        choice = input("\nSelect Option: ")

        # -----------------------------------
        # LIST USERS
        # -----------------------------------
        if choice == "1":

            users = users_service.get_all_users()

            print(f"\nTotal Users : {len(users)}\n")

            for user in users:
                print("----------------------------")
                print("ID       :", user.get("id"))
                print("Username :", user.get("username"))
                print("Email    :", user.get("email"))
                print("Enabled  :", user.get("enabled"))

        # -----------------------------------
        # CREATE USER
        # -----------------------------------
        elif choice == "2":

            username = input("Username : ")
            email = input("Email    : ")
            password = input("Password : ")

            response = users_service.create_user(
                username,
                email,
                password
            )

            if response.status_code == 201:

                print("\nUser Created Successfully.")

                AuditLogger.info(
                    f"Created user '{username}'"
                )

            else:

                print("\nFailed to create user.")
                print(response.text)

        # -----------------------------------
        # SEARCH USER
        # -----------------------------------
        elif choice == "3":

            username = input("\nEnter Username : ")

            users = users_service.search_user(username)

            if len(users) == 0:

                print("\nNo user found.")

            else:

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

        # -----------------------------------
        # UPDATE USER
        # -----------------------------------
        elif choice == "4":

            username = input("\nEnter Username : ")

            users = users_service.search_user(username)

            if len(users) == 0:

                print("\nUser not found.")

            else:

                user = users[0]

                print("\nCurrent Information")
                print("----------------------------")
                print("Username :", user.get("username"))
                print("Email    :", user.get("email"))

                new_email = input("\nNew Email : ")

                response = users_service.update_user(
                    user.get("id"),
                    user.get("username"),
                    new_email
                )

                if response.status_code == 204:

                    print("\nUser Updated Successfully.")

                    AuditLogger.info(
                        f"Updated user '{username}'"
                    )

                else:

                    print("\nFailed to update user.")
                    print(response.text)

        # -----------------------------------
        # DISABLE USER
        # -----------------------------------
        elif choice == "5":

            user_id = input("\nEnter User ID : ")

            response = users_service.disable_user(user_id)

            if response.status_code == 204:

                print("\nUser Disabled Successfully.")

                AuditLogger.info(
                    f"Disabled user '{user_id}'"
                )

            else:

                print("\nFailed to disable user.")
                print(response.text)

        # -----------------------------------
        # DELETE USER
        # -----------------------------------
        elif choice == "6":

            user_id = input("\nEnter User ID : ")

            response = users_service.delete_user(user_id)

            if response.status_code == 204:

                print("\nUser Deleted Successfully.")

                AuditLogger.info(
                    f"Deleted user '{user_id}'"
                )

            else:

                print("\nFailed to delete user.")
                print(response.text)

        # -----------------------------------
        # EXIT
        # -----------------------------------
        elif choice == "7":

            print("\nGood Bye!\n")
            break

        else:

            print("\nInvalid Option")


if __name__ == "__main__":
    main()