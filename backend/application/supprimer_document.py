from pathlib import Path

from app.extensions import db
from infrastructure.document_repository import DocumentRepository


def executer(document_id):
    """
    Supprime un document ainsi que son fichier physique.
    """

    document = DocumentRepository.trouver_par_id(document_id)

    if document is None:
        raise ValueError("Document introuvable")

    chemin = Path(document.chemin_fichier)

    if chemin.exists():
        chemin.unlink()

    DocumentRepository.supprimer(document)

    db.session.commit()