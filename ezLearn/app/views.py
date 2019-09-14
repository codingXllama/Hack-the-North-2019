# Insert views here

from ezLearn.app import app
from ezLearn.app.models import db, account
import random
from flask import redirect, render_template, url_for, session, request, flash


@app.route("/")
def index():
    return "yeet"


@app.route("/login")
def login():
    if request.method == 'POST':
        username = request.form('username')
        password = request.form('password')

        login = db.query.filter_by(
            username=username, password=password).first()

        if login is not None:
            redirect(url_for('index'))
        else:
            flash("Username or password is incorrect", "error")

    return render_template("login.html")


@app.route("/register")
def register():

    if request.method == 'POST':
        username = request.form("username")
        password = request.form("password")

        def get_rando_id():
            rando_id = random.randint(
                100000000000000000000000, 999999999999999999999999)
            check = db.Query.filter_by(account_id=str(rando_id)).first()
            if check is not None:
                get_rando_id()
            else:
                return str(rando_id)

        account_id = get_rando_id()

        register = account(username=username,
                           password=password, account_id=account_id)
        flash("You have successfully regestered")
        redirect(url_for("index"))
    return render_template("signup.html")
