from models.order_model import OrderModel
from models.menu_item_model import MenuItemModel

class OrderController:
    def __init__(self):
        self.order_model = OrderModel()
        self.menu_model = MenuItemModel()

    def place_order(self, customer_id):
        order_id = self.order_model.create_order(customer_id)
        if not order_id:
            print("Failed to create order.")
            return

        total = 0
        while True:
            print("\nAvailable Menu Items:")
            items = self.menu_model.get_all_items()
            for item in items:
                print(f"{item['item_id']}. {item['name']} - ₹{item['price']}")

            try:
                item_id = int(input("Enter Item ID to add (0 to finish): "))
                if item_id == 0:
                    break
                quantity = int(input("Enter quantity: "))
            except ValueError:
                print("Invalid input. Try again.")
                continue

            price = self.order_model.get_menu_item_price(item_id)
            if price is None:
                print("Invalid item ID.")
                continue

            subtotal = self.order_model.add_order_item(order_id, item_id, quantity, price)
            total += subtotal
            print(f"Added to order: ₹{subtotal:.2f}")

        self.order_model.update_order_total(order_id, total)
        print(f"\n Order placed successfully! Total: ₹{total:.2f} (Order ID: {order_id})")
