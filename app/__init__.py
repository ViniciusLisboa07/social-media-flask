# app/__init__.py
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

database = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    bcrypt = Bcrypt(app)
    login_manager = LoginManager(app)

    database.init_app(app)  # Inicializa o Flask-SQLAlchemy

    from .routes import main
    app.register_blueprint(main)

    return app
