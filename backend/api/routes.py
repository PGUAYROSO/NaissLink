from flask import Blueprint, jsonify, request, send_file

from application.recherche_sejour import executer as rechercher_sejour_service
from application.creer_dossier import executer as creer_dossier
from application.consulter_dossier import executer as consulter_dossier
from application.lister_dossiers import executer as lister_dossiers
from application.lister_documents import executer as lister_documents
from application.upload_document import executer as upload_document_service
from application.consulter_document import executer as consulter_document

from infrastructure.dossier_repository import DossierRepository

import os

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
# Recherche d'un séjour (Simulation DPI)
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

    dossier = creer_dossier(numero_sejour)

    if dossier is None:
        return jsonify({
            "message": "Un dossier documentaire existe déjà pour ce séjour."
        }), 409

    return jsonify(dossier.to_dict()), 201


# ------------------------------------------------------------------
# Consultation d'un dossier documentaire
# ------------------------------------------------------------------

@api.get("/dossiers/<numero_sejour>")
def consulter_dossier_route(numero_sejour):

    dossier = consulter_dossier(numero_sejour)

    if dossier is None:
        return jsonify({
            "message": "Dossier documentaire introuvable."
        }), 404

    return jsonify(dossier.to_dict())


# ------------------------------------------------------------------
# Liste des dossiers documentaires
# ------------------------------------------------------------------

@api.get("/dossiers")
def lister_dossiers_route():

    dossiers = lister_dossiers()

    return jsonify([
        dossier.to_dict()
        for dossier in dossiers
    ])


# ------------------------------------------------------------------
# Upload d'un document
# ------------------------------------------------------------------

@api.post("/documents/upload")
def upload_document_route():
    fichier = request.files.get("fichier")

    if fichier is None:
        return jsonify({
            "message": "Aucun fichier reçu."
        }), 400

    if fichier.filename == "":
        return jsonify({
            "message": "Aucun fichier sélectionné."
        }), 400

    numero_sejour = request.form.get("numero_sejour")
    type_document = request.form.get("type_document")

    if not numero_sejour:
        return jsonify({
            "message": "Le numéro de séjour est obligatoire."
        }), 400

    if not type_document:
        return jsonify({
            "message": "Le type de document est obligatoire."
        }), 400

    try:

        document = upload_document_service(
            numero_sejour=numero_sejour,
            type_document=type_document,
            fichier=fichier
        )

        return jsonify(document.to_dict()), 201

    except ValueError as e:

        return jsonify({
            "message": str(e)
        }), 400




    except Exception as e:
        import traceback

        traceback.print_exc()

        return jsonify({
            "message": "Erreur interne lors de l'enregistrement du document.",
            "erreur": str(e)
        }), 500


# ------------------------------------------------------------------
# Liste des documents d'un dossier documentaire
# ------------------------------------------------------------------

@api.get("/dossiers/<numero_sejour>/documents")
def lister_documents_route(numero_sejour):

    dossier = DossierRepository.trouver_par_numero_sejour(numero_sejour)

    if dossier is None:
        return jsonify({
            "message": "Dossier documentaire introuvable."
        }), 404

    documents = lister_documents(dossier.id)

    return jsonify([
        document.to_dict()
        for document in documents
    ])


# ------------------------------------------------------------------
# Consultation d'un document
# ------------------------------------------------------------------

@api.get("/documents/<int:document_id>")
def consulter_document_route(document_id):

    document = consulter_document(document_id)

    if document is None:
        return jsonify({
            "message": "Document introuvable."
        }), 404

    return jsonify(document.to_dict())


# ------------------------------------------------------------------
# Téléchargement d'un document
# ------------------------------------------------------------------

@api.get("/documents/<int:document_id>/download")
def telecharger_document_route(document_id):

    document = consulter_document(document_id)

    if document is None:
        return jsonify({
            "message": "Document introuvable."
        }), 404

    if not os.path.isfile(document.chemin_fichier):
        return jsonify({
            "message": "Le fichier est introuvable sur le serveur."
        }), 404

    return send_file(
        document.chemin_fichier,
        as_attachment=True,
        download_name=document.nom
    )