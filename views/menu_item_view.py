from controllers.menu_item_controller import MenuItemController

class MenuItemView:
    def __init__(self):
        self.controller = MenuItemController()

    def show_menu_item_menu(self):
        while True:
            print("\n----- Menu Item Menu -----")
            print("1. View All Menu Items")
            print("2. Add New Item")
            print("3. Delete Item")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.display_menu()
            elif choice == '2':
                self.add_menu_item()
            elif choice == '3':
                self.delete_menu_item()
            elif choice == '4':
                print("Exiting Menu Item Menu...")
                break
            else:
                print("Invalid choice. Try again.")

    def display_menu(self):
        items = self.controller.view_menu()
        if items:
            print("\n--- Menu Items ---")
            for item in items:
                print(f"{item['item_id']}: {item['name']} - ₹{item['price']}")
        else:
            print("No items found.")

    def add_menu_item(self):
        print("\n--- Add New Menu Item ---")
        name = input("Enter item name: ")
        desc = input("Enter description: ")
        price = float(input("Enter price: "))
        item_id = self.controller.add_menu_item(name, desc, price)
        print(f"Item added with ID: {item_id}")

    def delete_menu_item(self):
        print("\n--- Delete Menu Item ---")
        item_id = input("Enter item ID to delete: ")
        deleted = self.controller.delete_menu_item(item_id)
        if deleted:
            print("Item deleted.")
        else:
            print("Item not found.")
