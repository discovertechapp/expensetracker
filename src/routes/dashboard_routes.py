from flask import Blueprint, request

from src.services.dashboard_service import (
    get_dashboard_summary,
    get_monthly_summary
)

dashboard_bp = Blueprint("dashboard_bp", __name__)


# ---------------------------------------------------------
# Dashboard Summary
# ---------------------------------------------------------
@dashboard_bp.route("/dashboard", methods=["GET"])
def dashboard():

    user_id = request.args.get("user_id")

    response = get_dashboard_summary(user_id)

    return response


# ---------------------------------------------------------
# Monthly Summary
# ---------------------------------------------------------
@dashboard_bp.route(
    "/dashboard/monthly-summary",
    methods=["GET"]
)
def monthly_summary():

    user_id = request.args.get("user_id")

    response = get_monthly_summary(user_id)

    return response
