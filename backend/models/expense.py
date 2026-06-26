from database import get_db_connection


class Expense:

    @staticmethod
    def add_expense(user_id, title, amount, category,
                    expense_date, description):

        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO expenses
        (user_id, title, amount, category,
        expense_date, description)
        VALUES(?,?,?,?,?,?)
        """

        cursor.execute(
            query,
            (
                user_id,
                title,
                amount,
                category,
                expense_date,
                description
            )
        )

        conn.commit()

        cursor.close()
        conn.close()

    @staticmethod
    def get_expenses(user_id):

        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
        SELECT * FROM expenses
        WHERE user_id=?
        ORDER BY expense_date DESC
        """

        cursor.execute(query, (user_id,))

        data = cursor.fetchall()

        cursor.close()
        conn.close()

        return [dict(row) for row in data]

    @staticmethod
    def delete_expense(expense_id):

        conn = get_db_connection()
        cursor = conn.cursor()

        query = "DELETE FROM expenses WHERE id=?"

        cursor.execute(query, (expense_id,))

        conn.commit()

        cursor.close()
        conn.close()

    @staticmethod
    def update_expense(
        expense_id,
        title,
        amount,
        category,
        expense_date,
        description
    ):

        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
        UPDATE expenses
        SET title=?,
            amount=?,
            category=?,
            expense_date=?,
            description=?
        WHERE id=?
        """

        cursor.execute(
            query,
            (
                title,
                amount,
                category,
                expense_date,
                description,
                expense_id
            )
        )

        conn.commit()

        cursor.close()
        conn.close()