from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import random
import collections
from flask import redirect, render_template, url_for, session, request, flash
import bleach
import html2text

app = Flask(__name__)

headings_topic_words = []

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "YouSmellLikeJatin"
db = SQLAlchemy(app)


class account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(48), unique=True)
    full_name = db.Column(db.String(128))
    password = db.Column(db.String(64))
    account_id = db.Column(db.String(6))
    created_duos = db.Column(db.Integer)
    created_notes = db.Column(db.Integer)
    # Maybe add names and more personal stuff later

class duo(db.Model):  # This is a db entry for pairs of question and answers in a highlighted document
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    question = db.Column(db.String(400))
    answer = db.Column(db.String(400))
    duo_id = db.Column(db.String(64))
    author = db.Column(db.String(6))

class note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    content = db.Column(db.String(3500))
    note_id = db.Column(db.String(64))
    subject = db.Column(db.String(128))
    author = db.Column(db.String(6))

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
            return redirect(url_for('dashboard', account_id=login.account_id))
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
                100000, 999999)
            check = db.session.query(account).filter_by(account_id=str(rando_id)).first()
            if check is not None:
                get_rando_id()
            else:
                return str(rando_id)

        account_id = get_rando_id()
        registerer = account(full_name = full_name, username=username, password=password, account_id=account_id, created_notes = 0, created_duos = 0)
        db.session.add(registerer)
        db.session.commit()
        flash("You have successfully registered")
        return redirect(url_for("dashboard", account_id = registerer.account_id))
    return render_template("signup.html")

# Insert View Note Function!

@app.route("/<int:account_id>/dashboard")
def dashboard(account_id):
    int(account_id)
    user = db.session.query(account).filter_by(account_id = str(account_id)).first()
    notes = []
    #for note in range(int(user.created_duos)):
        #notes.append(db.session.query(note).filter_by(note_id = int(account_id) + note).first())
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
    duos = db.session.query(duo).filter_by(author=account_id).all()
    noted = db.session.query(note).filter_by(author=account_id).all()
    return render_template('dashboard.html', account_id=account_id, notes=noted, duos=duos)


@app.route("/<int:account_id>/notebook/write", methods=["POST", "GET"])
def write(account_id):
    if request.method == "POST":
        notez = request.form.get("content")
        subject = request.form.get("subject")
        title = request.form.get("title")
        notez = html2text.html2text(notez)
        user = db.session.query(account).filter_by(account_id=account_id).first()
        def genNote_ID():
            user.created_notes += 1
            return str(user.account_id) + str(user.created_notes)
        the_one = genNote_ID()
        notez = unformat(notez)
        to_upload = note(title=title, content=notez, subject=subject, note_id=the_one, author=account_id)
        create_duos(notez, account_id)
        db.session.add(to_upload)
        db.session.commit()
        duos = db.session.query(duo).filter_by(author=account_id).all()
        noted = db.session.query(note).filter_by(author=account_id).all()
        return render_template('dashboard.html', account_id=int(user.account_id), duos=duos, notes=noted)
    return render_template('notebook_writer.html')

@app.route('/<int:account_id>/notebook/learn', methods=["POST", "GET"])
def learn(account_id):
    duos = db.session.query(duo).filter_by(author=account_id).all()
    return render_template('notebook_learn.html', duos=duos)

@app.route('/<int:account_id>/notebook/test', methods=["POST", "GET"])
def test(account_id):
    def create_questions():
        duo = db.session.query(duo).filter_by(author=account_id).first()
        duos = db.session.query(duo).filter_by(duo_id=duo.duo_id).all()
        questions = []
        result = []
        coll_ans = []
        answers = []
        for item in duos:
            questions.append(item.question)
            answers.append(item.answer)
        temp_ans = []
        for answer in answers:
            temp_ans.append(answer)
            for i in range(3):
                rnd = random.choice(answers) if rnd is not temp_ans[0] else "None of the Above"
                temp_ans.append(rnd) 
            random.shuffle(temp_ans)
            coll_ans.append(temp_ans)
            temp_ans = []      
        for i in range(len(coll_ans)):
            result.append((coll_ans[i]), questions[i])
        return result

    if request.method == "POST":
        answer = request.form['radio']
    quiz = create_questions()
    return render_template('notebook_test.html', questions=quiz, account_id=account_id)

def create_duos(text, account_id):
    #globals
    global headings_topic_words
    #Setup
    text = unformat(text)
    #Topic Word Declaration
    starred = return_starred(text, 2)
    for word in starred:
        headings_topic_words.append(word)
    bolded = return_bold(text)
    for word in bolded:
        headings_topic_words.append(word)
    italics = return_italics(text)
    for word in italics:
        headings_topic_words.append(word)
    marked = return_marked(text)
    for word in marked:
        headings_topic_words.append(word)
    headered = return_headers(text)
    for word in headered:
        headings_topic_words.append(word)
    # Topic word sorting
    headings_bunshin = headings_topic_words
    counts = collections.Counter(headings_bunshin)
    headings_topic_words = sorted(headings_bunshin, key=lambda x: (counts[x], x), reverse=True)
    # Pick up Questions
    question_str = return_quest_punct(text)
    text.replace(question_str, "")
    questions = []
    questions.append(question_str)
    for i in range(100):
        question_str = return_quest_punct(text)
        questions.append(question_str)
    # Pick up answers
    answers = []
    for question in questions:
        answer = return_statement(text, question)
        answers.append(answer)
    # Create Duos
    user = db.session.query(account).filter_by(account_id=account_id).first()
    for i in range(len(answers)):
        to_upload = duo(title=questions[i], question=questions[i], answer=answers[i], author=account_id, duo_id=account_id+user.created_duos)
        user.created_duos += 1
        db.session.add(to_upload)
        db.session.commit()
    
def return_starred(text, count):
    if count > 1:
        starred = []
    words = text.split(" ")
    for i in range(len(words)):
        word = words[i]
        if word.count("*") > 0:
            word.replace("*", "")
            if count == 1:
                return word
            else:
                starred.append(word)
    return starred
            
def return_bold(text):
    # This will return an array of all bolded words
    words = text.split(" ")
    bolded = []
    count = []
    final = []
    for i in range(len(words)):
        word = words[i]
        if word.count("<b>") > 1:
            word.replace("<b>", "")
            word.replace("</b>", "")
            bolded.append(word)
    
    for item in bolded:
        count.append((bolded.count(item), item))
    
    for i in range(len(count)):
        min_val = min(count[i][0])
        final.append(min_val[1])
        count.remove(min_val)

    return final

def return_italics(text):
    words = text.split(" ")
    bolded = []
    count = []
    final = []
    for i in range(len(words)):
        word = words[i]
        if word.count("<i>") > 1:
            word.replace("<i>", "")
            word.replace("</i>", "")
            bolded.append(word)
    
    for item in bolded:
        count.append((bolded.count(item), item))
    
    for i in range(len(count)):
        min_val = min(count[i][0])
        final.append(min_val[1])
        count.remove(min_val)

    return final

def return_headers(text):
    words = text.split(" ")
    bolded = []
    count = []
    final = []
    for i in range(len(words)):
        word = words[i]
        if word.count("<h") > 1:
            word.replace("<h", "")
            word.replace("</h", "")
            word.replace("1>", "")
            word.replace("2>", "")
            word.replace("3>", "")
            word.replace("4>", "")
            word.replace("5>", "")
            word.replace("6>", "")
            bolded.append(word)
    
    for item in bolded:
        count.append((bolded.count(item), item))
    
    for i in range(len(count)):
        min_val = min(count[i][0])
        final.append(min_val[1])
        count.remove(min_val)

    return final

def return_marked(text):
    words = text.split(" ")
    bolded = []
    count = []
    final = []
    for i in range(len(words)):
        word = words[i]
        if word.count("<mark>") > 1:
            word.replace("<mark>", "")
            word.replace("</mark>", "")
            bolded.append(word)
    
    for item in bolded:
        count.append((bolded.count(item), item))
    
    for i in range(len(count)):
        min_val = min(count[i][0])
        final.append(min_val[1])
        count.remove(min_val)

    return final


def return_quest_punct(text):
    words = text.split(" ")
    current_index = 0
    past_index = 0
    for i in range(len(words)):
        word = words[i]
        if word.count("?") > 0:
            current_index = i
            for j in range(0, current_index):
                if words[j].count(".") > 0:
                    past_index = j
                break
            break
    
    quest_sent = words[past_index:current_index]
    quest_str = ""
    for word in quest_sent:
        quest_str = quest_str + " " + word
    return quest_str

def return_quest(text: str):
    text.lower()
    words = text.split(" ")
    start_index = 0
    end_index = 0
    for i in range(len(words)):
        word = words[i]
        buzzWords = ['solve', 'compute', 'determine', 'explain', 'do']
        if word in buzzWords:
            for j in range(0, i):
                if words[j].count('.') > 0:
                    start_index = j
                break
            for j in range(i, len(words)):
                if words[j].count('.') > 0:
                    end_index = j
                break
            break
    quest_list = words[start_index:end_index]
    quest_str = ""
    for item in quest_list:
        quest_str = quest_str + " " + item
    return quest_str

def return_statement(text: str, question: str):
    question.replace('?', '')
    question.lower()
    quest_list = question.split(" ")
    words = text.split(" ")
    start_index = 0
    end_index = 0
    for i in range(len(words)):
        word = words[i]
        buzzWords = ["answer", "solution",
                            "key", "result", "justification"]
        # if word.lower() == "answer" or word.lower() == "solution" or word.lower:
        if word.lower() in buzzWords:
            for j in range(0, i):
                if words[j].count('.') > 0:
                    start_index = j
                break
            for j in range(i, len(words)):
                if words[j].count('.') > 0:
                    end_index = j
                break
            break
    statement_sentance = words[start_index:end_index]
    statement = ""
    for word in statement_sentance:
        statement = statement + " " + word
    return statement

def pattern_finder(text):
    big_dict = open("1-1000.txt", "r")
    big_list = big_dict.split("/n")
    big_dict.close()
    text = unformat(text)
    altered = []
    yes = []
    final = []
    ward = []
    count = []
    words = text.split(" ")
    for word in words:
        if word in big_list:
            del(word)
        else:
            altered.append(word)
    for word in altered:
        count.append((altered.count(word)))
        yes.append(word)
        for i in range(len(altered.count(word))):
            del(word)
    true_final = []
    for i in range(len(count)):
        final.append(max(count))
        ward.append(altered[count.index(max(count))])
        true_final.append((final[i], ward[i]))
        count.remove(max(count))

    return true_final

def unformat(para):
    para.replace("<b>", "")
    para.replace("</b>", "")
    para.replace("<i>", "")
    para.replace("</i>", "")
    para.replace("<mark>", "")
    para.replace("</mark>", "")
    para.replace("<h", "")
    para.replace("</h", "")
    para.replace("1>", "")
    para.replace("2>", "")
    para.replace("3>", "")
    para.replace("4>", "")
    para.replace("5>", "")
    para.replace("6>", "")
    para.replace("<em>", "")
    para.replace("</em>", "")
    return para



if __name__ == "__main__":
    app.run(debug=True)
