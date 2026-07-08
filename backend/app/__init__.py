from flask import Flask

from app.errors import register_error_handlers
from app.extensions import db, migrate, jwt

from api.routes import api
from api.auth_routes import auth
from api.utilisateurs_routes import utilisateurs

import domain.dossier
import domain.document
import domain.utilisateur
import domain.audit_log


def create_app():

    app = Flask(__name__)

    app.config.from_object("app.config.Config")

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    register_error_handlers(app)

    # ------------------------------------------------------------------
    # Blueprints
    # ------------------------------------------------------------------

    app.register_blueprint(api, url_prefix="/api")
    app.register_blueprint(auth, url_prefix="/api")
    app.register_blueprint(utilisateurs, url_prefix="/api")

    return app