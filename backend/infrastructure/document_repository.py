from app.extensions import db
from domain.document import Document


class DocumentRepository:

    @staticmethod
    def creer(
        dossier_id,
        nom,
        type_document,
        chemin_fichier,
        taille
    ):

        document = Document(
            dossier_id=dossier_id,
            nom=nom,
            type_document=(
                type_document.value
                if hasattr(type_document, "value")
                else type_document
            ),
            chemin_fichier=chemin_fichier,
            taille=taille
        )

        db.session.add(document)
        return document

    @staticmethod
    def trouver_par_id(document_id):

        return db.session.get(Document, document_id)

    @staticmethod
    def trouver_par_dossier(dossier_id):

        return (
            Document.query
            .filter_by(dossier_id=dossier_id)
            .order_by(Document.date_upload.desc())
            .all()
        )

    @staticmethod
    def supprimer(document):

        db.session.delete(document)