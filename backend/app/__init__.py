from flask import Flask

from app.extensions import db, migrate
from api.routes import api
from app.errors import register_error_handlers

import domain.dossier
import domain.document


def create_app():
    app = Flask(__name__)

    app.config.from_object("app.config.Config")

    db.init_app(app)
    migrate.init_app(app, db)

    register_error_handlers(app)

    app.register_blueprint(api, url_prefix="/api")