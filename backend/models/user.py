from database import get_db_connection


class User:

    @staticmethod
    def create_user(username, email, password):
        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO users(username, email, password)
        VALUES(?, ?, ?)
        """

        cursor.execute(query, (username, email, password))

        conn.commit()

        cursor.close()
        conn.close()

    @staticmethod
    def get_user_by_email(email):
        conn = get_db_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM users WHERE email=?"

        cursor.execute(query, (email,))

        user = cursor.fetchone()

        cursor.close()
        conn.close()

        return dict(user) if user else None