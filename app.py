from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import Config  # Importa a classe de configuração
from models import models  # Importa a classe de configuração
from flask_cors import CORS
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user


app = Flask(__name__)

# Configuração do banco de dados usando a classe Config
app.config.from_object(Config)
login_manager = LoginManager()
# Inicializando o SQLAlchemy com a configuração do Flask
db = SQLAlchemy(app)
login_manager.init_app(app)
login_manager.login_view = 'login'
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello World'

# Criação das tabelas e execução da aplicação
if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Criar todas as tabelas no banco de dados
    app.run(debug=True)