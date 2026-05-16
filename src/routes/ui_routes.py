from flask import Blueprint, render_template

ui_bp = Blueprint(
    "ui_bp",
    __name__
)


@ui_bp.route("/")
def login_page():

    return render_template(
        "login.html"
    )


@ui_bp.route("/dashboard-ui")
def dashboard_page():

    return render_template(
        "dashboard.html"
    )
