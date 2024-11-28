from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import Config  # Importa a classe de configuração
from flask_cors import CORS
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from datetime import datetime

# Inicializando a aplicação Flask
app = Flask(__name__)

# Configuração do banco de dados usando a classe Config
app.config.from_object(Config)
login_manager = LoginManager()
# Inicializando o SQLAlchemy com a configuração do Flask
db = SQLAlchemy(app)
login_manager.init_app(app)
login_manager.login_view = 'login'
CORS(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    available = db.Column(db.Boolean, default=True)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    loan_date = db.Column(db.DateTime, default=datetime.utcnow)
    return_date = db.Column(db.DateTime, nullable=True)


@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  

    app.run(debug=True)
