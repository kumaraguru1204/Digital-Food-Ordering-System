from config.db_config import get_connection

class BaseModel:
    def __init__(self):
        self.conn = get_connection()
        self.cursor = self.conn.cursor(dictionary=True)

    def __del__(self):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()