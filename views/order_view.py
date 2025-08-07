from controllers.order_controller import OrderController

class OrderView:
    def __init__(self):
        self.order_controller = OrderController()

    def show_order_menu(self):
        print("\n==== Place New Order ====")
        try:
            customer_id = int(input("Enter Customer ID: "))
            self.order_controller.place_order(customer_id)
        except ValueError:
            print("Invalid customer ID. Please enter a number.")
