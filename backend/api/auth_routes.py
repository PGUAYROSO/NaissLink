# ------------------------------------------------------------------
# Flask
# ------------------------------------------------------------------

from flask import Blueprint, request

# ------------------------------------------------------------------
# JWT
# ------------------------------------------------------------------

from flask_jwt_extended import (
    create_access_token,
    jwt_required
)

# ------------------------------------------------------------------
# Réponses API
# ------------------------------------------------------------------

from app.responses import success, error

# ------------------------------------------------------------------
# Application
# ------------------------------------------------------------------

from application.creer_utilisateur import executer as creer_utilisateur
from application.authentifier import executer as authentifier
from application.journaliser_action import executer as journaliser_action

# ------------------------------------------------------------------
# Security
# ------------------------------------------------------------------

from security.decorators import roles_required
from security.permissions import ROLE_ADMIN

auth = Blueprint("auth", __name__)


# ------------------------------------------------------------------
# Création d'un utilisateur
# ------------------------------------------------------------------

@auth.post("/utilisateurs")
@jwt_required()
@roles_required(ROLE_ADMIN)
def creer_utilisateur_route():

    data = request.get_json(silent=True)

    if data is None:
        return error(
            "Le corps de la requête est invalide.",
            400
        )

    champs = [
        "nom",
        "prenom",
        "login",
        "email",
        "mot_de_passe",
        "role"
    ]

    for champ in champs:

        if not data.get(champ):

            return error(
                f"Le champ '{champ}' est obligatoire.",
                400
            )

    try:

        utilisateur = creer_utilisateur(
            nom=data["nom"],
            prenom=data["prenom"],
            login=data["login"],
            email=data["email"],
            mot_de_passe=data["mot_de_passe"],
            role=data["role"]
        )

        journaliser_action(
            utilisateur=data["login"],
            action="CREATE_UTILISATEUR",
            objet=data["email"]
        )

        return success(
            utilisateur.to_dict(),
            201
        )

    except ValueError as e:

        return error(
            str(e),
            409
        )


# ------------------------------------------------------------------
# Authentification
# ------------------------------------------------------------------

@auth.post("/auth/login")
def login():

    data = request.get_json()

    login = data.get("login")
    mot_de_passe = data.get("mot_de_passe")

    if not login or not mot_de_passe:
        return error(
            "Login ou mot de passe manquant.",
            400
        )

    utilisateur = authentifier(
        login,
        mot_de_passe
    )

    if utilisateur is None:
        return error(
            "Login ou mot de passe incorrect.",
            401
        )

    access_token = create_access_token(
        identity=str(utilisateur.id),
        additional_claims={
            "login": utilisateur.login,
            "role": utilisateur.role
        }
    )

    journaliser_action(
        utilisateur=utilisateur.login,
        action="LOGIN",
        objet="Authentification"
    )

    return success(
        {
            "access_token": access_token,
            "utilisateur": utilisateur.to_dict()
        }
    )