from flask import Blueprint, request, jsonify
from models.expense import Expense


expense_bp = Blueprint("expense", __name__)


@expense_bp.route("/expenses", methods=["POST"])
def add_expense():
    data = request.get_json(silent=True) or {}

    required_fields = ["user_id", "title", "amount", "category", "expense_date"]
    missing = [field for field in required_fields if str(data.get(field, "")).strip() == ""]

    if missing:
        return jsonify({
            "message": f"Missing required fields: {', '.join(missing)}"
        }), 400

    Expense.add_expense(
        data["user_id"],
        data["title"],
        float(data["amount"]),
        data["category"],
        data["expense_date"],
        data.get("description", "")
    )

    return jsonify({
        "message": "Expense added successfully"
    })


@expense_bp.route("/expenses/<int:user_id>",
                   methods=["GET"])
def get_expenses(user_id):

    expenses = Expense.get_expenses(user_id)

    return jsonify(expenses)


@expense_bp.route("/expenses/<int:expense_id>",
                   methods=["DELETE"])
def delete_expense(expense_id):

    Expense.delete_expense(expense_id)

    return jsonify({
        "message": "Expense deleted successfully"
    })


@expense_bp.route("/expenses/<int:expense_id>",
                   methods=["PUT"])
def update_expense(expense_id):
    data = request.get_json(silent=True) or {}

    Expense.update_expense(
        expense_id,
        data["title"],
        float(data["amount"]),
        data["category"],
        data["expense_date"],
        data.get("description", "")
    )

    return jsonify({
        "message": "Expense updated successfully"
    })