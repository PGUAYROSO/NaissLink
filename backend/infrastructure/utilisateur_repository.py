from app.extensions import db
from domain.utilisateur import Utilisateur


class UtilisateurRepository:

    @staticmethod
    def creer(utilisateur):
        db.session.add(utilisateur)
        db.session.commit()

        return utilisateur

    @staticmethod
    def trouver_par_login(login: str):
        return (
            Utilisateur.query
            .filter_by(login=login)
            .first()
        )

    @staticmethod
    def trouver_par_email(email: str):
        return (
            Utilisateur.query
            .filter_by(email=email)
            .first()
        )

    @staticmethod
    def trouver_par_id(utilisateur_id: int):
        return Utilisateur.query.get(utilisateur_id)

    @staticmethod
    def trouver_tous():
        return (
            Utilisateur.query
            .order_by(
                Utilisateur.nom,
                Utilisateur.prenom
            )
            .all()
        )

    @staticmethod
    def mettre_a_jour():
        db.session.commit()

    @staticmethod
    def supprimer(utilisateur):
        db.session.delete(utilisateur)
        db.session.commit()