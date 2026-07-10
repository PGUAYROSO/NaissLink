from app.extensions import db
from domain.transmission import Transmission


class TransmissionRepository:

    @staticmethod
    def creer(transmission):

        db.session.add(transmission)
        db.session.commit()

        return transmission

    @staticmethod
    def trouver_par_id(transmission_id: int):

        return Transmission.query.get(transmission_id)

    @staticmethod
    def trouver_toutes():

        return (
            Transmission.query
            .order_by(
                Transmission.date_envoi.desc()
            )
            .all()
        )

    @staticmethod
    def trouver_par_dossier(dossier_id: int):

        return (
            Transmission.query
            .filter_by(dossier_id=dossier_id)
            .order_by(
                Transmission.date_envoi.desc()
            )
            .all()
        )

    @staticmethod
    def sauvegarder():

        db.session.commit()

    @staticmethod
    def supprimer(transmission):

        db.session.delete(transmission)
        db.session.commit()