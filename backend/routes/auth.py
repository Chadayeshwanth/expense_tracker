from flask import Blueprint, request, jsonify
from models.user import User
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash


auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json(silent=True) or {}

    username = (data.get("username") or "").strip()
    email = (data.get("email") or "").strip().lower()
    password = (data.get("password") or "").strip()

    if not username or not email or not password:
        return jsonify({
            "message": "Missing required fields"
        }), 400

    existing_user = User.get_user_by_email(email)

    if existing_user:
        return jsonify({
            "message": "Email already exists"
        }), 400

    hashed_password = generate_password_hash(password)

    User.create_user(
        username,
        email,
        hashed_password
    )

    return jsonify({
        "message": "User registered successfully"
    })


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json(silent=True) or {}

    email = (data.get("email") or "").strip().lower()
    password = (data.get("password") or "").strip()

    if not email or not password:
        return jsonify({
            "message": "Please provide email and password"
        }), 400

    user = User.get_user_by_email(email)

    if not user:
        return jsonify({
            "message": "Invalid credentials"
        }), 401

    if not check_password_hash(
            user["password"],
            password):

        return jsonify({
            "message": "Invalid credentials"
        }), 401

    return jsonify({
        "message": "Login successful",
        "user_id": user["id"],
        "username": user["username"]
    })