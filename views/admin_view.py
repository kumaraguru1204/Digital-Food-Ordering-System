from controllers.admin_controller import AdminController

class AdminView:
    def __init__(self):
        self.admin_controller = AdminController()

    def show_admin_menu(self):
        while True:
            print("\n==== Admin Menu ====")
            print("1. Create Admin")
            print("2. Login")
            print("3. Back to Main Menu")
            choice = input("Choose: ")

            if choice == '1':
                self.admin_controller.create_admin()
            elif choice == '2':
                success = self.admin_controller.login()
                if success:
                    print("Use main menu options to manage menu items.")
            elif choice == '3':
                break
            else:
                print("Invalid choice.")
