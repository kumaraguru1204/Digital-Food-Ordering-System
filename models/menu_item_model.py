from models.base_model import BaseModel

class MenuItemModel(BaseModel):
    def get_all_items(self):
        try:
            self.cursor.execute("SELECT * FROM Menu_Item")
            return self.cursor.fetchall()
        except Exception as e:
            print("Error fetching menu items:", e)
            return []

    def get_item_by_id(self, item_id):
        try:
            query = "SELECT * FROM Menu_Item WHERE item_id = %s"
            self.cursor.execute(query, (item_id,))
            return self.cursor.fetchone()
        except Exception as e:
            print("Error getting item:", e)
            return None

    def add_item(self, name, description, price):
        try:
            query = "INSERT INTO Menu_Item (name, description, price) VALUES (%s, %s, %s)"
            self.cursor.execute(query, (name, description, price))
            self.conn.commit()
            return self.cursor.lastrowid
        except Exception as e:
            print("Error adding menu item:", e)
            return None

    def delete_item(self, item_id):
        try:
            query = "DELETE FROM Menu_Item WHERE item_id = %s"
            self.cursor.execute(query, (item_id,))
            self.conn.commit()
            return self.cursor.rowcount
        except Exception as e:
            print("Error deleting item:", e)
            return 0
