from models.base_model import BaseModel

class AdminModel(BaseModel):
    def add_admin(self, username, password):
        try:
            query = "INSERT INTO Admin (username, password) VALUES (%s, %s)"
            self.cursor.execute(query, (username, password))
            self.conn.commit()
            print("Admin added successfully.")
        except Exception as e:
            print("Error adding admin:", e)

    def authenticate_admin(self, username, password):
        try:
            query = "SELECT * FROM Admin WHERE username = %s AND password = %s"
            self.cursor.execute(query, (username, password))
            return self.cursor.fetchone()
        except Exception as e:
            print("Error logging in:", e)
            return None
