from flask import Blueprint

diary_bp = Blueprint("diary_bp", __name__)


@diary_bp.route("/diary")
def diary():
    return {
        "status": True,
        "message": "Diary Route Working"
    }
