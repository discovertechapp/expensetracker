from flask import Blueprint, request

from src.services.diary_service import (
    create_diary_entry,
    get_diary_entries
)

diary_bp = Blueprint("diary_bp", __name__)


# ---------------------------------------------------------
# Create Diary Entry
# ---------------------------------------------------------
@diary_bp.route("/diary", methods=["POST"])
def add_diary():

    payload = request.json

    response = create_diary_entry(payload)

    return response


# ---------------------------------------------------------
# Get Diary Entries
# ---------------------------------------------------------
@diary_bp.route("/diary", methods=["GET"])
def diary():

    user_id = request.args.get("user_id")

    response = get_diary_entries(user_id)

    return response
