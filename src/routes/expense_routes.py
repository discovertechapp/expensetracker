from flask import Blueprint, request

from src.services.expense_service import (
    create_expense,
    get_expenses,
    update_expense,
    delete_expense,
    search_expenses
)
from src.utils.auth_middleware import token_required
expense_bp = Blueprint("expense_bp", __name__)


# ---------------------------------------------------------
# Create Expense
# ---------------------------------------------------------
@expense_bp.route("/expenses", methods=["POST"])
@token_required
def add_expense():

    payload = request.json

    response = create_expense(payload)

    return response


# ---------------------------------------------------------
# Get Expenses
# ---------------------------------------------------------
@expense_bp.route("/expenses", methods=["GET"])
@token_required
def expenses():

    user_id = request.args.get("user_id")

    response = get_expenses(user_id)

    return response


# ---------------------------------------------------------
# Update Expense
# ---------------------------------------------------------
@expense_bp.route(
    "/expenses/<document_id>",
    methods=["PUT"]
)
@token_required
def edit_expense(document_id):

    payload = request.json

    response = update_expense(
        document_id,
        payload
    )

    return response


# ---------------------------------------------------------
# Delete Expense
# ---------------------------------------------------------
@expense_bp.route(
    "/expenses/<document_id>",
    methods=["DELETE"]
)
@token_required
def remove_expense(document_id):

    response = delete_expense(document_id)

    return response


# ---------------------------------------------------------
# Search Expenses
# ---------------------------------------------------------
@expense_bp.route(
    "/expenses/search",
    methods=["GET"]
)
@token_required
def expense_search():

    user_id = request.args.get("user_id")

    main_category = request.args.get(
        "main_category"
    )

    start_date = request.args.get(
        "start_date"
    )

    end_date = request.args.get(
        "end_date"
    )

    response = search_expenses(
        user_id,
        main_category,
        start_date,
        end_date
    )

    return response
