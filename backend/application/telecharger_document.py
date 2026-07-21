from pathlib import Path

from application.repository.DocumentRepository import DocumentRepository


class TelechargerDocumentService:

    @staticmethod
    def executer(document_id):

        document = DocumentRepository.rechercher_par_id(document_id)

        if document is None:
            raise ValueError("Document introuvable")

        chemin = Path(document.chemin)

        if not chemin.exists():
            raise ValueError("Fichier introuvable")

        return document, chemin