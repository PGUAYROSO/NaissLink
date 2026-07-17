import os

from flask import current_app

from domain.type_document import CodeTypeDocument

from infrastructure.dossier_repository import DossierRepository
from infrastructure.stockage_fichiers import StockageFichiers

from application.creer_document import executer as creer_document


def executer(
    numero_sejour: str,
    type_document: str,
    fichier
):

    dossier = DossierRepository.trouver_par_numero_sejour(numero_sejour)

    if dossier is None:
        raise ValueError("Dossier documentaire introuvable.")

    print("type_document reçu :", repr(type_document))

    try:
        type_document = CodeTypeDocument[type_document]
    except KeyError:
        print("Valeurs autorisées :", [e.name for e in CodeTypeDocument])
        raise ValueError(f"Type de document invalide : {type_document}")

    dossier_destination = os.path.join(
        current_app.config["UPLOAD_FOLDER"],
        numero_sejour
    )

    chemin = StockageFichiers.enregistrer(
        fichier,
        dossier_destination
    )

    return creer_document(
        dossier.id,
        fichier.filename,
        type_document,
        chemin,
        os.path.getsize(chemin)
    )