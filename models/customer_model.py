from models.base_model import BaseModel

class CustomerModel(BaseModel):
    def add_customer(self, name, phone, email):
        try:
            query = """
            INSERT INTO Customer (name, phone_number, email)
            VALUES (%s, %s, %s)
            """
            self.cursor.execute(query, (name, phone, email))
            self.conn.commit()
            return self.cursor.lastrowid
        except Exception as e:
            print("Error adding customer:", e)
            return None

    def get_customer_by_phone(self, phone):
        try:
            query = "SELECT * FROM Customer WHERE phone_number = %s"
            self.cursor.execute(query, (phone,))
            return self.cursor.fetchone()
        except Exception as e:
            print("Error fetching customer:", e)
            return None

    def get_all_customers(self):
        try:
            self.cursor.execute("SELECT * FROM Customer")
            return self.cursor.fetchall()
        except Exception as e:
            print("Error getting customers:", e)
            return []
