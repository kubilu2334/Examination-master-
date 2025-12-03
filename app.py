from flask import Flask, render_template, request, redirect, url_for, flash, send_file
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    token = db.Column(db.String(200), unique=True, nullable=False)

# Routes
@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    token = request.form.get('token')

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password) and user.token == token:
        return redirect(url_for('dashboard'))
    else:
        flash('Invalid credentials or token')
        return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    pdf_path = os.path.join('static', 'example.pdf')
    return render_template('dashboard.html', pdf_path=pdf_path)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
cat > app.py
from flask import Flask, render_template, request, redirect, url_for, flash, send_file
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    token = db.Column(db.String(200), unique=True, nullable=False)

# Routes
@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    token = request.form.get('token')

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password) and user.token == token:
        return redirect(url_for('dashboard'))
    else:
        flash('Invalid credentials or token')
        return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    pdf_path = os.path.join('static', 'example.pdf')
    return render_template('dashboard.html', pdf_path=pdf_path)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
