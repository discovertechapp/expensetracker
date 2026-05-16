from flask import Blueprint

expense_bp = Blueprint("expense_bp", __name__)


@expense_bp.route("/expenses")
def expenses():
    return {
        "status": True,
        "message": "Expense Route Working"
    }
