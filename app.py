from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import db, User, Note
from forms import LoginForm, RegisterForm, NoteForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# @app.before_first_request
# def create_tables():
#     db.create_all()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash("Registration successful! Please login.")
        return redirect(url_for('login'))
    return render_template("register.html", form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
        if user:
            login_user(user)
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid username or password")
    return render_template("login.html", form=form)

@app.route('/dashboard')
@login_required
def dashboard():
    notes = Note.query.filter_by(user_id=current_user.id).all()
    return render_template("dashboard.html", notes=notes)

@app.route('/add', methods=['GET', 'POST'])
@login_required
def add_note():
    form = NoteForm()
    if form.validate_on_submit():
        new_note = Note(title=form.title.data, content=form.content.data, user_id=current_user.id)
        db.session.add(new_note)
        db.session.commit()
        flash("Note added successfully!")
        return redirect(url_for("dashboard"))
    return render_template("add_note.html", form=form)

@app.route('/delete/<int:note_id>')
@login_required
def delete(note_id):
    note = Note.query.get(note_id)
    if note and note.user_id == current_user.id:
        db.session.delete(note)
        db.session.commit()
        flash("Note deleted!")
    return redirect(url_for("dashboard"))

@app.route('/edit/<int:note_id>', methods=['GET', 'POST'])
@login_required
def edit_note(note_id):
    note = Note.query.get(note_id)
    if note and note.user_id == current_user.id:
        form = NoteForm(obj=note)   # Pre-fill form with note data
        if form.validate_on_submit():
            note.title = form.title.data
            note.content = form.content.data
            db.session.commit()
            flash("Note updated successfully!")
            return redirect(url_for("dashboard"))
        return render_template("add_note.html", form=form, edit=True)
    flash("Note not found or unauthorized")
    return redirect(url_for("dashboard"))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)