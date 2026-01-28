from flask import Blueprint, render_template, request, redirect
from flask_login import login_user, logout_user
from app.models.user import User
from app.extensions import db
from app.utils.security import hash_password, verify_password
import random
import string

auth = Blueprint("auth", __name__)

@auth.route("/", methods=["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(email=email).first()

        if not user:
            error = "You are not registered yet. Please register first."
        elif not verify_password(password, user.password):
            error = "Invalid credentials"
        else:
            login_user(user)
            return redirect("/dashboard")

    return render_template("login.html", error=error)


@auth.route("/register", methods=["GET", "POST"])
def register():
    error = None

    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        if User.query.filter_by(email=email).first():
            error = "You are already registered."
        else:
            user = User(email=email, password=hash_password(password))
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect("/dashboard")

    return render_template("register.html", error=error)


@auth.route("/forgot-password", methods=["GET", "POST"])
def forgot_password():
    new_password = None

    if request.method == "POST":
        email = request.form["email"]
        user = User.query.filter_by(email=email).first()

        if user:
            temp_pass = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            user.password = hash_password(temp_pass)
            db.session.commit()
            new_password = temp_pass
        else:
            new_password = "Email not registered"

    return render_template("forgot_password.html", new_password=new_password)


@auth.route("/logout")
def logout():
    logout_user()
    return redirect("/")
