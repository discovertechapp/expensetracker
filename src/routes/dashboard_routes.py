from flask import Blueprint

dashboard_bp = Blueprint("dashboard_bp", __name__)


@dashboard_bp.route("/dashboard")
def dashboard():
    return {
        "status": True,
        "message": "Dashboard Route Working"
    }
