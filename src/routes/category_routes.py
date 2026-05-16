from flask import Blueprint, request

from src.services.category_service import (
    create_category,
    get_categories
)

category_bp = Blueprint("category_bp", __name__)


# ---------------------------------------------------------
# Create Category
# ---------------------------------------------------------
@category_bp.route("/categories", methods=["POST"])
def add_category():

    payload = request.json

    response = create_category(payload)

    return response


# ---------------------------------------------------------
# Get Categories
# ---------------------------------------------------------
@category_bp.route("/categories", methods=["GET"])
def categories():

    response = get_categories()

    return response
