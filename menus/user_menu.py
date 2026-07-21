from operations.users.list_users import ListUsersOperation
from core.logger import AuditLogger
from operations.users.create_user import CreateUserOperation
from operations.users.search_user import SearchUserOperation

class UserMenu:

    def __init__(self, api):

        self.api = api

    def start(self):

        while True:

            print("\n" + "=" * 50)
            print("        USER MANAGEMENT")
            print("=" * 50)

            print("1. List Users")
            print("2. Create User")
            print("3. Search User")
            print("4. Update User")
            print("5. Disable User")
            print("6. Delete User")
            print("7. Back")

            choice = input("\nSelect Option : ")

            if choice == "1":
                
                ListUsersOperation(self.api).execute()

            elif choice == "2":
                CreateUserOperation(self.api).execute()

            elif choice == "3":
                SearchUserOperation(self.api).execute()

            elif choice == "4":
                self.update_user()

            elif choice == "5":
                self.disable_user()

            elif choice == "6":
                self.delete_user()

            elif choice == "7":
                break

            else:
                print("\nInvalid Option")