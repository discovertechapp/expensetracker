from flask import Blueprint, request

from src.services.expense_service import add_expense

expense_bp = Blueprint("expense_bp", __name__)


@expense_bp.route("/expenses", methods=["GET"])
def expenses():

    return {
        "status": True,
        "message": "Expense Route Working"
    }


@expense_bp.route("/expenses", methods=["POST"])
def create_expense():

    payload = request.json

    response = add_expense(payload)

    return response
