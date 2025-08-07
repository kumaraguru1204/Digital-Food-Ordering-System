from models.customer_model import CustomerModel

class CustomerController:
    def __init__(self):
        self.model = CustomerModel()

    def register_customer(self, name, phone, email):
        existing = self.model.get_customer_by_phone(phone)
        if existing:
            print("\nCustomer already registered!")
            return existing
        else:
            customer_id = self.model.add_customer(name, phone, email)
            print("\nCustomer registered successfully!")
            return {"customer_id": customer_id, "name": name, "phone": phone, "email": email}

    def get_customer_details(self, phone):
        customer = self.model.get_customer_by_phone(phone)
        if customer:
            print("\nCustomer found.")
            return customer
        else:
            print("\nNo customer found with this phone.")
            return None