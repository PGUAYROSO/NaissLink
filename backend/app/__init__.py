from flask import Flask
from flask_cors import CORS

from app.errors import register_error_handlers
from app.extensions import db, migrate, jwt


from api.auth_routes import auth
from api.utilisateurs_routes import utilisateurs
from api.transmission_routes import transmissions
from api.type_document_routes import types_documents
from api.administration_routes import administration
from api.dossiers_routes import dossiers
from api.documents_routes import documents

import domain.dossier
import domain.document
import domain.utilisateur
import domain.audit_log
import domain.transmission
import domain.type_document


def create_app():
    app = Flask(__name__)

    app.config.from_object("app.config.Config")

    app.register_blueprint(types_documents, url_prefix="/api")

    CORS(
        app,
        resources={r"/api/*": {"origins": "http://localhost:5173"}}
    )

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    register_error_handlers(app)

    app.register_blueprint(auth, url_prefix="/api")
    app.register_blueprint(utilisateurs, url_prefix="/api")
    app.register_blueprint(transmissions, url_prefix="/api")
    app.register_blueprint(administration, url_prefix="/api")
    app.register_blueprint(dossiers, url_prefix="/api")
    app.register_blueprint(documents, url_prefix="/api")

    app.app_context().push()

    return app