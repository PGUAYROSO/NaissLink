from flask import Blueprint, jsonify, request

from flask_jwt_extended import (
    jwt_required,
    get_jwt
)

from application.journaliser_action import executer as journaliser_action

from application.creer_type_document import executer as creer_type_document
from application.consulter_type_document import executer as consulter_type_document
from application.lister_types_documents import executer as lister_types_documents
from application.modifier_type_document import executer as modifier_type_document
from application.supprimer_type_document import executer as supprimer_type_document


types_documents = Blueprint(
    "types_documents",
    __name__
)


# ------------------------------------------------------------------
# Liste
# ------------------------------------------------------------------

@types_documents.get("/types-documents")
@jwt_required()
def lister():

    types = lister_types_documents()

    return jsonify([
        t.to_dict()
        for t in types
    ])


# ------------------------------------------------------------------
# Consultation
# ------------------------------------------------------------------

@types_documents.get("/types-documents/<int:type_document_id>")
@jwt_required()
def consulter(type_document_id):

    type_document = consulter_type_document(
        type_document_id
    )

    if type_document is None:

        return jsonify({
            "message": "Type de document introuvable."
        }), 404

    return jsonify(
        type_document.to_dict()
    )


# ------------------------------------------------------------------
# Création
# ------------------------------------------------------------------

@types_documents.post("/types-documents")
@jwt_required()
def creer():

    data = request.get_json()

    if data is None:

        return jsonify({
            "message": "Corps de requête invalide."
        }), 400

    type_document = creer_type_document(

        code=data["code"],

        libelle=data["libelle"],

        description=data.get("description"),

        ordre=data.get("ordre", 0)

    )

    if type_document is None:

        return jsonify({
            "message": "Ce code existe déjà."
        }), 409

    claims = get_jwt()

    journaliser_action(

        utilisateur=claims["login"],

        action="CREER_TYPE_DOCUMENT",

        objet=type_document.code

    )

    return jsonify(
        type_document.to_dict()
    ), 201


# ------------------------------------------------------------------
# Modification
# ------------------------------------------------------------------

@types_documents.put("/types-documents/<int:type_document_id>")
@jwt_required()
def modifier(type_document_id):

    data = request.get_json()

    type_document = modifier_type_document(

        type_document_id,

        data["code"],

        data["libelle"],

        data.get("description"),

        data.get("ordre", 0),

        data.get("actif", True)

    )

    if type_document is None:

        return jsonify({
            "message": "Type de document introuvable."
        }), 404

    claims = get_jwt()

    journaliser_action(

        utilisateur=claims["login"],

        action="MODIFIER_TYPE_DOCUMENT",

        objet=type_document.code

    )

    return jsonify(
        type_document.to_dict()
    )


# ------------------------------------------------------------------
# Suppression
# ------------------------------------------------------------------

@types_documents.delete("/types-documents/<int:type_document_id>")
@jwt_required()
def supprimer(type_document_id):

    ok = supprimer_type_document(
        type_document_id
    )

    if not ok:

        return jsonify({
            "message": "Type de document introuvable."
        }), 404

    claims = get_jwt()

    journaliser_action(

        utilisateur=claims["login"],

        action="SUPPRIMER_TYPE_DOCUMENT",

        objet=str(type_document_id)

    )

    return "", 204