import os
from flask import Flask
from app.models import db  # db is imported from models.py, where it is defined


def create_app():
    app = Flask(__name__)  # Create the Flask app object
    app.config['SECRET_KEY'] = 'development'

    # Update the database URI to point to the db folder
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'db', 'yourdatabase.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'  # SQLite file in the db folder


    # Initialize the database with the app
    db.init_app(app)  # Bind the db (SQLAlchemy) instance to the app

    return app
