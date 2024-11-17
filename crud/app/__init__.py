from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)

    with app.app_context():
        from app.routes import register_routes
        register_routes(app)  # Registra as rotas
        db.create_all()       # Cria as tabelas no banco, se não existirem

    return app
