from views.customer_view import CustomerView
from views.menu_item_view import MenuItemView
from views.order_view import OrderView
from views.admin_view import AdminView 

def main_menu():
    while True:
        print("\n==== Main Menu ====")
        print("1. Customer Section")
        print("2. Menu Item Section")
        print("3. Place Order")
        print("4. Admin Section")
        print("5. Exit")
        choice = input("Choose: ")

        if choice == '1':
            CustomerView().show_menu()
        elif choice == '2':
            MenuItemView().show_menu_item_menu()
        elif choice == '3':
            OrderView().show_order_menu()
        elif choice == '4':
            AdminView().show_admin_menu()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    main_menu() 