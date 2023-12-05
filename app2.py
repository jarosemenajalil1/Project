from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Use SQLite for simplicity
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Sample data (you'll replace this with a database later)
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ratings = db.relationship('Rating', backref='course', lazy=True)

class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    difficulty = db.Column(db.Integer, nullable=False)
    usefulness = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/")
def index():
    courses = Course.query.all()
    return render_template("index.html", courses=courses)

@app.route("/rate/<int:course_id>", methods=["GET", "POST"])
@login_required
def rate_course(course_id):
    course = Course.query.get_or_404(course_id)

    if request.method == "POST":
        difficulty = int(request.form.get("difficulty"))
        usefulness = int(request.form.get("usefulness"))
        comment = request.form.get("comment")

        # Save the rating and comment to the database
        new_rating = Rating(difficulty=difficulty, usefulness=usefulness, comment=comment, course=course)
        db.session.add(new_rating)
        db.session.commit()

        return redirect(url_for("index"))

    return render_template("rate_course.html", course=course)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            login_user(user)
            flash("Login successful", "success")
            return redirect(url_for("index"))
        else:
            flash("Login unsuccessful. Check your username and password.", "danger")

    return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

