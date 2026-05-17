from flask import Blueprint, render_template

ui_bp = Blueprint(
    "ui_bp",
    __name__
)


# ---------------------------------------------------------
# Login Page
# ---------------------------------------------------------
@ui_bp.route("/")
def login_page():

    return render_template(
        "login.html"
    )


# ---------------------------------------------------------
# Signup Page
# ---------------------------------------------------------
@ui_bp.route("/signup")
def signup_page():

    return render_template(
        "signup.html"
    )


# ---------------------------------------------------------
# Dashboard Page
# ---------------------------------------------------------
@ui_bp.route("/dashboard-ui")
def dashboard_page():

    return render_template(
        "dashboard.html"
    )
