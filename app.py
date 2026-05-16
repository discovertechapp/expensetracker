from flask import Flask

from src.routes.auth_routes import auth_bp
from src.routes.expense_routes import expense_bp
from src.routes.dashboard_routes import dashboard_bp
from src.routes.diary_routes import diary_bp

from src.utils.index_manager import create_indices
from src.services.auth_service import create_default_admin

app = Flask(__name__)

app.config['SECRET_KEY'] = 'expense_tracker_secret'

# Register Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(expense_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(diary_bp)


@app.route("/")
def home():

    return {
        "status": True,
        "message": "Expense Tracker Running Successfully"
    }


if __name__ == "__main__":

    # Create Elasticsearch indices
    create_indices()

    # Create default admin
    create_default_admin()

    app.run(
        debug=True,
        host="0.0.0.0",
        port=5001
    )
