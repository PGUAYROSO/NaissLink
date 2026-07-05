from domain.dossier import DossierDocumentaire
from app.extensions import db


class DossierRepository:

    @staticmethod
    def creer(numero_sejour: str):

        dossier = DossierDocumentaire(
            numero_sejour=numero_sejour
        )

        db.session.add(dossier)
        db.session.commit()

        return dossier

    @staticmethod
    def trouver_par_numero_sejour(numero_sejour: str):

        return (
            DossierDocumentaire.query
            .filter_by(numero_sejour=numero_sejour)
            .first()
        )

    @staticmethod
    def trouver_tous():

        return (
            DossierDocumentaire.query
            .order_by(DossierDocumentaire.date_creation.desc())
            .all()
        )