import os

from flask import current_app

from domain.type_document import TypeDocument

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

    try:
        type_document = TypeDocument[type_document]
    except KeyError:
        raise ValueError("Type de document invalide.")

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