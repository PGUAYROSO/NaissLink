from app.extensions import db
from infrastructure.document_repository import DocumentRepository


def executer(
    dossier_id,
    nom,
    type_document,
    chemin_fichier,
    taille
):

    document = DocumentRepository.creer(
        dossier_id=dossier_id,
        nom=nom,
        type_document=type_document,
        chemin_fichier=chemin_fichier,
        taille=taille,
    )

    db.session.commit()

    return document