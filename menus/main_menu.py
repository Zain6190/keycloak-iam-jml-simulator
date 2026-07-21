from menus.user_menu import UserMenu


class MainMenu:

    def __init__(self, api):

        self.api = api

    def start(self):

        while True:

            print("\n" + "=" * 50)
            print("         KEYCLOAK IAM CONSOLE")
            print("=" * 50)

            print("1. User Management")
            print("2. Group Management")
            print("3. Role Management")
            print("4. JML Workflow")
            print("5. Exit")

            choice = input("\nSelect Option : ")

            if choice == "1":

                UserMenu(self.api).start()

            elif choice == "2":

                print("\nGroup Management - Coming Soon")

            elif choice == "3":

                print("\nRole Management - Coming Soon")

            elif choice == "4":

                print("\nJML Workflow - Coming Soon")

            elif choice == "5":

                print("\nGood Bye!\n")
                break

            else:

                print("\nInvalid Option")