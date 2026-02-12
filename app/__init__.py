from flask import Flask
from app.config import Config
from app.infrastructure.db.extensions import db, migrate
from app.infrastructure import models
from app.presentation.v1.routes.auth import auth_bp
from dotenv import load_dotenv
load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    print("DB URI =", app.config.get("SQLALCHEMY_DATABASE_URI"))
    
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(auth_bp)

    return app

app = create_app()