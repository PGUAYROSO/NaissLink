from app.extensions import db

from domain.type_document import TypeDocument


class TypeDocumentRepository:

    @staticmethod
    def creer(
            code: str,
            libelle: str,
            description: str = None,
            ordre: int = 0
    ):

        type_document = TypeDocument(
            code=code,
            libelle=libelle,
            description=description,
            ordre=ordre
        )

        db.session.add(type_document)
        db.session.commit()

        return type_document

    @staticmethod
    def trouver_par_id(type_document_id: int):

        return db.session.get(
            TypeDocument,
            type_document_id
        )

    @staticmethod
    def trouver_par_code(code: str):

        return (
            TypeDocument.query
            .filter_by(code=code)
            .first()
        )

    @staticmethod
    def lister():

        return (
            TypeDocument.query
            .order_by(
                TypeDocument.ordre.asc(),
                TypeDocument.libelle.asc()
            )
            .all()
        )

    @staticmethod
    def modifier(type_document):

        db.session.commit()

        return type_document

    @staticmethod
    def supprimer(type_document):

        db.session.delete(type_document)

        db.session.commit()