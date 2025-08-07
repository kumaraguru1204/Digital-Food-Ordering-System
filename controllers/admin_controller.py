from models.admin_model import AdminModel

class AdminController:
    def __init__(self):
        self.admin_model = AdminModel()

    def create_admin(self):
        username = input("Enter new admin username: ")
        password = input("Enter password: ")
        self.admin_model.add_admin(username, password)

    def login(self):
        username = input("Admin username: ")
        password = input("Password: ")
        admin = self.admin_model.authenticate_admin(username, password)
        if admin:
            print(f"\nWelcome, {admin['username']}!")
            return True
        else:
            print("Invalid credentials.")
            return False
