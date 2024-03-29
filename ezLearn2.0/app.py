from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import random
from flask import redirect, render_template, url_for, session, request, flash

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "YouSmellLikeJatin"
db = SQLAlchemy(app)

class account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(48), unique=True)
    full_name = db.Column(db.String(128))
    password = db.Column(db.String(64))
    account_id = db.Column(db.String(24))
    created_duos = db.Column(db.Integer)
    # Maybe add names and more personal stuff later

class duo(db.Model):  # This is a db entry for pairs of question and answers in a highlighted document
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    question = db.Column(db.String(400))
    answer = db.Column(db.String(400))
    duo_id = db.Column(db.String(64))

class note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    content = db.Column(db.String(3500))
    note_id = db.Column(db.String(64))
    subject = db.Column(db.String(128))

@app.route("/")
def index():
    return redirect(url_for('login'))



@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        if not request.form.get('username') or not request.form.get('password'):
            flash("Please enter all you information", 'error')
            return redirect(url_for('login'))
        username = request.form.get('username')
        password = request.form.get('password')

        login = db.session.query(account).filter_by(username=username, password=password).first()

        if login is not None:
            return redirect(url_for('register'))
        else:
            flash("Username or password is incorrect", "error")
            return redirect(url_for('login'))

    return render_template("login.html")


@app.route("/signup", methods=["POST", "GET"])
def register():
    if request.method == 'POST':
        if not request.form.get('full_name') or not request.form.get('username') or not request.form.get('password'):
            flash("Please enter all you information", 'error')
            return redirect(url_for('register'))
        full_name = request.form.get('full_name')
        username = request.form.get('username')
        password = request.form.get("password")
        def get_rando_id():
            rando_id = random.randint(
                100000000000000000000000, 999999999999999999999999)
            check = db.session.query(account).filter_by(account_id=str(rando_id)).first()
            if check is not None:
                get_rando_id()
            else:
                return str(rando_id)

        account_id = get_rando_id()

        registerer = account(full_name = full_name, username=username, password=password, account_id=account_id)
        db.session.add(registerer)
        db.session.commit()
        flash("You have successfully registered")
        return redirect(url_for("dashboard"))
    return render_template("signup.html")

@app.route("/<int:account_id>/dashboard")
def dashboard(account_id):
    int(account_id)
    user = db.session.query(account).filter_by(account_id = str(account_id)).first()
    notes = []
    for note in int(user.created_duos):
        notes.append(db.session.query(note).filter_by(note_id = int(account_id) + note).first())
    # Insert Jinja loop based on the notes
    
    # Also have an Ajax command to help load up a delete note command
    # Here is the function
    def remove_duo(id):
        note_to_del = db.session.query(duo).filter_by(duo_id = id).first()
        db.session.remove(note_to_del)
        db.session.commit()
    def remove_note(id):
        note_to_del = db.session.query(note).filter_by(note_id = id).first()
        db.session.remove(note_to_del)
        db.session.commit()
    return render_template('dashboard.html')

@app.route('/<int:account_id>/new_note')
def new_note(account_id):
    int(account_id)
    user = db.session.query(account).filter_by(account_id = int(account_id)).first()
    # Getting the quill elements and such
    # Not possible 'til AJAX is done
    return render_template('new_note.html')

@app.route("/<int:account_id>/<int:note_id>/<int:duo_id>/learn")
def learn(account_id, note_id, duo_id):
    int(account_id)
    int(note_id)
    int(duo_id)

    # JINJA CODE 2BD

if __name__ == "__main__":
    app.run(debug=True)
