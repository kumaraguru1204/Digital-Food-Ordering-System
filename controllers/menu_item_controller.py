from models.menu_item_model import MenuItemModel

class MenuItemController:
    def __init__(self):
        self.model = MenuItemModel()

    def view_menu(self):
        return self.model.get_all_items()

    def get_item(self, item_id):
        return self.model.get_item_by_id(item_id)

    def add_menu_item(self, name, description, price):
        return self.model.add_item(name, description, price)

    def delete_menu_item(self, item_id):
        return self.model.delete_item(item_id)
