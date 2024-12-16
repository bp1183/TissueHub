import os
from flask import Flask
from app.models import db
from app.routes import index, collection_details, new_collection, new_sample


def create_app(testing=False):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'development'

    if testing:
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    else:
        db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'db', 'tissuehub.db')
        app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'

    # Bind the db (SQLAlchemy) instance to the app
    db.init_app(app)

    # Register routes
    app.add_url_rule("/", "index", index)
    app.add_url_rule("/collections/<int:collection_id>", "collection_details", collection_details)
    app.add_url_rule("/collections/new", "new_collection", new_collection, methods=["GET", "POST"])
    app.add_url_rule("/collections/<int:collection_id>/samples/new", "new_sample", new_sample, methods=["GET", "POST"])

    return app
