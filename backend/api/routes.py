from flask import Blueprint, jsonify, request

from application.recherche_sejour import executer as rechercher_sejour_service
from application.creer_dossier import executer as creer_dossier
from application.consulter_dossier import executer as consulter_dossier
from application.lister_dossiers import executer as lister_dossiers

api = Blueprint("api", __name__)


# ------------------------------------------------------------------
# Santé de l'application
# ------------------------------------------------------------------

@api.get("/health")
def health():
    return jsonify({
        "application": "NaissLink",
        "version": "1.0.0",
        "status": "UP"
    })


# ------------------------------------------------------------------
# Recherche d'un séjour (simulation DPI)
# ------------------------------------------------------------------

@api.get("/sejours/<numero_sejour>")
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

@api.post("/dossiers")
def creer():

    data = request.get_json()

    if not data or "numero_sejour" not in data:
        return jsonify({
            "message": "Le numéro de séjour est obligatoire."
        }), 400

    dossier = creer_dossier(data["numero_sejour"])

    if dossier is None:
        return jsonify({
            "message": "Un dossier documentaire existe déjà pour ce séjour."
        }), 409

    return jsonify(dossier.to_dict()), 201


# ------------------------------------------------------------------
# Consultation d'un dossier documentaire
# ------------------------------------------------------------------

@api.get("/dossiers/<numero_sejour>")
def consulter(numero_sejour):

    dossier = consulter_dossier(numero_sejour)

    if dossier is None:
        return jsonify({
            "message": "Dossier introuvable."
        }), 404

    return jsonify(dossier.to_dict())


# ------------------------------------------------------------------
# Liste de tous les dossiers documentaires
# ------------------------------------------------------------------

@api.get("/dossiers")
def lister():

    dossiers = lister_dossiers()

    return jsonify([
        dossier.to_dict()
        for dossier in dossiers
    ])