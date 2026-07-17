import traceback

from flask import Blueprint, jsonify, request

from flask_jwt_extended import (
    jwt_required,
    get_jwt
)

from application.journaliser_action import executer as journaliser_action
from application.recherche_sejour import executer as rechercher_sejour_service
from application.creer_dossier import executer as creer_dossier
from application.consulter_dossier import executer as consulter_dossier
from application.lister_dossiers import executer as lister_dossiers

dossiers = Blueprint("dossiers", __name__)


# ------------------------------------------------------------------
# Recherche d'un séjour (Simulation DPI)
# ------------------------------------------------------------------

@dossiers.get("/sejours/<numero_sejour>")
def rechercher_sejour(numero_sejour):

    sejour = rechercher_sejour_service(numero_sejour)

    if sejour is None:
        return jsonify({
            "message": "Séjour introuvable."
        }), 404

    return jsonify({
        "numero_sejour": sejour.numero_sejour,
        "nom_mere": sejour.nom_mere,
        "prenom_mere": sejour.prenom_mere,
        "nom_enfant": sejour.nom_enfant,
        "date_naissance": sejour.date_naissance
    })


# ------------------------------------------------------------------
# Création d'un dossier documentaire
# ------------------------------------------------------------------

@dossiers.post("/dossiers")
@jwt_required()
def creer_dossier_route():

    data = request.get_json(silent=True)

    if data is None:
        return jsonify({
            "message": "Le corps de la requête est invalide."
        }), 400

    numero_sejour = data.get("numero_sejour")

    if not numero_sejour:
        return jsonify({
            "message": "Le numéro de séjour est obligatoire."
        }), 400

    claims = get_jwt()

    dossier = creer_dossier(
        numero_sejour=numero_sejour,
        cree_par=claims["login"]
    )

    if dossier is None:
        return jsonify({
            "message": "Un dossier documentaire existe déjà pour ce séjour."
        }), 409

    journaliser_action(
        utilisateur=claims["login"],
        action="CREATE_DOSSIER",
        objet=numero_sejour
    )

    return jsonify(dossier.to_dict()), 201


# ------------------------------------------------------------------
# Consultation d'un dossier
# ------------------------------------------------------------------

@dossiers.get("/dossiers/<numero_sejour>")
@jwt_required()
def consulter_dossier_route(numero_sejour):

    dossier = consulter_dossier(numero_sejour)

    if dossier is None:
        return jsonify({
            "message": "Dossier documentaire introuvable."
        }), 404

    claims = get_jwt()

    journaliser_action(
        utilisateur=claims["login"],
        action="CONSULTER_DOSSIER",
        objet=numero_sejour
    )

    return jsonify(dossier.to_dict())


# ------------------------------------------------------------------
# Liste des dossiers
# ------------------------------------------------------------------

@dossiers.get("/dossiers")
@jwt_required()
def lister_dossiers_route():

    dossiers_liste = lister_dossiers()

    return jsonify([
        dossier.to_dict()
        for dossier in dossiers_liste
    ])