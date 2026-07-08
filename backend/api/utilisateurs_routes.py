# ------------------------------------------------------------------
# Flask
# ------------------------------------------------------------------

from flask import Blueprint

# ------------------------------------------------------------------
# JWT
# ------------------------------------------------------------------

from flask_jwt_extended import jwt_required

# ------------------------------------------------------------------
# Réponses API
# ------------------------------------------------------------------

from app.responses import success

# ------------------------------------------------------------------
# Application
# ------------------------------------------------------------------

from application.lister_utilisateurs import executer as lister_utilisateurs

# ------------------------------------------------------------------
# Security
# ------------------------------------------------------------------

from security.decorators import roles_required
from security.permissions import ROLE_ADMIN

utilisateurs = Blueprint("utilisateurs", __name__)


# ------------------------------------------------------------------
# Liste des utilisateurs
# ------------------------------------------------------------------

@utilisateurs.get("/utilisateurs")
@jwt_required()
@roles_required(ROLE_ADMIN)
def lister_utilisateurs_route():

    utilisateurs_liste = lister_utilisateurs()

    return success([
        utilisateur.to_dict()
        for utilisateur in utilisateurs_liste
    ])