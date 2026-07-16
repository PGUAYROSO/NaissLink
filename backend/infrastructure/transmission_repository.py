from domain.transmission import Transmission
from app.extensions import db


class TransmissionRepository:

    @staticmethod
    def creer(transmission):

        db.session.add(transmission)
        db.session.commit()

        return transmission

    @staticmethod
    def trouver_par_id(transmission_id):

        return Transmission.query.get(transmission_id)

    @staticmethod
    def lister_par_dossier(dossier_id):

        return (
            Transmission.query
            .filter_by(dossier_id=dossier_id)
            .order_by(Transmission.date_creation.desc())
            .all()
        )

    @staticmethod
    def supprimer(transmission):

        db.session.delete(transmission)
        db.session.commit()