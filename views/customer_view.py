from controllers.customer_controller import CustomerController

class CustomerView:
    def __init__(self):
        self.controller = CustomerController()

    def show_menu(self):
        while True:
            print("\n----- Customer Menu -----")
            print("1. Register New Customer")
            print("2. Search Customer by Phone")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.register_customer()
            elif choice == '2':
                self.search_customer()
            elif choice == '3':
                print("Exiting Customer Menu...")
                break
            else:
                print("Invalid choice. Try again.")

    def register_customer(self):
        print("\n--- Register New Customer ---")
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        result = self.controller.register_customer(name, phone, email)
        print("Registered:", result)

    def search_customer(self):
        print("\n--- Search Customer ---")
        phone = input("Enter Phone Number: ")
        customer = self.controller.get_customer_details(phone)
        if customer:
            print("Customer Details:")
            print(customer)
