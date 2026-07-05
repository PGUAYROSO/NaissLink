from flask import Flask

from app.extensions import db
from api.routes import api

import domain.dossier
import domain.document


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "postgresql+psycopg://postgres:postgres@localhost:5432/naisslink"
    )

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    app.register_blueprint(api, url_prefix="/api")

    return app