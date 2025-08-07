from models.base_model import BaseModel

class OrderModel(BaseModel):
    def create_order(self, customer_id):
        try:
            query = "INSERT INTO Order_Table (customer_id, total_amount) VALUES (%s, %s)"
            self.cursor.execute(query, (customer_id, 0))  # Temporary total, updated later
            self.conn.commit()
            return self.cursor.lastrowid
        except Exception as e:
            print("Error creating order:", e)
            return None

    def add_order_item(self, order_id, item_id, quantity, item_price):
        try:
            subtotal = quantity * item_price
            query = """
                INSERT INTO Order_Item (order_id, item_id, quantity, subtotal)
                VALUES (%s, %s, %s, %s)
            """
            self.cursor.execute(query, (order_id, item_id, quantity, subtotal))
            self.conn.commit()
            return subtotal
        except Exception as e:
            print("Error adding order item:", e)
            return 0

    def update_order_total(self, order_id, total_amount):
        try:
            query = "UPDATE Order_Table SET total_amount = %s WHERE order_id = %s"
            self.cursor.execute(query, (total_amount, order_id))
            self.conn.commit()
        except Exception as e:
            print("Error updating order total:", e)

    def get_menu_item_price(self, item_id):
        try:
            query = "SELECT price FROM Menu_Item WHERE item_id = %s"
            self.cursor.execute(query, (item_id,))
            result = self.cursor.fetchone()
            return float(result['price']) if result else None
        except Exception as e:
            print("Error fetching price:", e)
            return None
