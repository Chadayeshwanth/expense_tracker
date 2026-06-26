from flask import Flask
from flask_cors import CORS

from routes.auth import auth_bp
from routes.expenses import expense_bp

from config import SECRET_KEY


app = Flask(__name__)

app.config["SECRET_KEY"] = SECRET_KEY

CORS(app)


app.register_blueprint(auth_bp, url_prefix="/api")
app.register_blueprint(expense_bp, url_prefix="/api")


@app.route("/")
def home():
    return {
        "message": "Expense Tracker API Running"
    }


if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )