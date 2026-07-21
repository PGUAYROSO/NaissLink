from domain.historique_transmission import HistoriqueTransmission


class HistoriqueTransmissionRepository:

    @staticmethod
    def ajouter(historique):

        from app.extensions import db

        db.session.add(historique)
        db.session.flush()

        return historique

    @staticmethod
    def lister_par_transmission(transmission_id):

        return (
            HistoriqueTransmission.query
            .filter_by(transmission_id=transmission_id)
            .order_by(HistoriqueTransmission.date_action.asc())
            .all()
        )