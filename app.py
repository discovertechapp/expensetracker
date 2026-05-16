from flask import Flask

from src.routes.auth_routes import auth_bp

app = Flask(__name__)

app.config['SECRET_KEY'] = 'expense_tracker_secret'

# Register Blueprints
app.register_blueprint(auth_bp)


@app.route("/")
def home():
    return {
        "status": True,
        "message": "Expense Tracker Running Successfully"
    }


if __name__ == "__main__":
    app.run(debug=True)
