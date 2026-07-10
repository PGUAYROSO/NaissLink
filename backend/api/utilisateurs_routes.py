# ------------------------------------------------------------------
# Flask
# ------------------------------------------------------------------

from flask import Blueprint, request

# ------------------------------------------------------------------
# JWT
# ------------------------------------------------------------------

from flask_jwt_extended import jwt_required

# ------------------------------------------------------------------
# Réponses API
# ------------------------------------------------------------------

from app.responses import success, error

# ------------------------------------------------------------------
# Security
# ------------------------------------------------------------------

from security.decorators import roles_required
from security.permissions import ROLE_ADMIN

# ------------------------------------------------------------------
# Application
# ------------------------------------------------------------------

from application.lister_utilisateurs import executer as lister_utilisateurs
from application.modifier_utilisateur import executer as modifier_utilisateur
from application.journaliser_action import executer as journaliser_action

utilisateurs = Blueprint("utilisateurs", __name__)

# ------------------------------------------------------------------
# Réinitialisation du Password
# ------------------------------------------------------------------
from application.reinitialiser_mot_de_passe import (
    executer as reinitialiser_mot_de_passe
)


# ------------------------------------------------------------------
# Activation / Désactivation d'un utilisateur
# ------------------------------------------------------------------

from application.modifier_etat_utilisateur import (
    executer as modifier_etat_utilisateur
)
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


# ------------------------------------------------------------------
# Modification d'un utilisateur
# ------------------------------------------------------------------

@utilisateurs.put("/utilisateurs/<int:utilisateur_id>")
@jwt_required()
@roles_required(ROLE_ADMIN)
def modifier_utilisateur_route(utilisateur_id):

    data = request.get_json(silent=True)

    if data is None:
        return error(
            "Le corps de la requête est invalide.",
            400
        )

    champs = [
        "nom",
        "prenom",
        "email",
        "role",
        "actif"
    ]

    for champ in champs:

        if champ not in data:

            return error(
                f"Le champ '{champ}' est obligatoire.",
                400
            )

    utilisateur = modifier_utilisateur(
        utilisateur_id=utilisateur_id,
        nom=data["nom"],
        prenom=data["prenom"],
        email=data["email"],
        role=data["role"],
        actif=data["actif"]
    )

    if utilisateur is None:

        return error(
            "Utilisateur introuvable.",
            404
        )

    journaliser_action(
        utilisateur=utilisateur.login,
        action="MODIFIER_UTILISATEUR",
        objet=utilisateur.email
    )

    return success(utilisateur.to_dict())

# ------------------------------------------------------------------
# Réinitialisation du mot de passe
# ------------------------------------------------------------------

@utilisateurs.patch("/utilisateurs/<int:utilisateur_id>/password")
@jwt_required()
@roles_required(ROLE_ADMIN)
def reinitialiser_mot_de_passe_route(utilisateur_id):

    data = request.get_json(silent=True)

    if data is None:

        return error(
            "Le corps de la requête est invalide.",
            400
        )

    mot_de_passe = data.get("mot_de_passe")

    if not mot_de_passe:

        return error(
            "Le mot de passe est obligatoire.",
            400
        )

    utilisateur = reinitialiser_mot_de_passe(
        utilisateur_id=utilisateur_id,
        mot_de_passe=mot_de_passe
    )

    if utilisateur is None:

        return error(
            "Utilisateur introuvable.",
            404
        )

    journaliser_action(
        utilisateur=utilisateur.login,
        action="RESET_PASSWORD",
        objet=utilisateur.email
    )

    return success({
        "message": "Mot de passe réinitialisé avec succès."
    })

# ------------------------------------------------------------------
# Activation / Désactivation d'un utilisateur
# ------------------------------------------------------------------

@utilisateurs.patch("/utilisateurs/<int:utilisateur_id>/actif")
@jwt_required()
@roles_required(ROLE_ADMIN)
def modifier_etat_utilisateur_route(utilisateur_id):

    data = request.get_json(silent=True)

    if data is None:
        return error(
            "Le corps de la requête est invalide.",
            400
        )

    if "actif" not in data:
        return error(
            "Le champ 'actif' est obligatoire.",
            400
        )

    try:

        utilisateur = modifier_etat_utilisateur(
            utilisateur_id=utilisateur_id,
            actif=data["actif"]
        )

        if utilisateur is None:
            return error(
                "Utilisateur introuvable.",
                404
            )

        journaliser_action(
            utilisateur=utilisateur.login,
            action="MODIFIER_ETAT_UTILISATEUR",
            objet=str(utilisateur.actif)
        )

        return success({
            "message": "État de l'utilisateur mis à jour.",
            "actif": utilisateur.actif
        })

    except ValueError as e:

        return error(
            str(e),
            409
        )