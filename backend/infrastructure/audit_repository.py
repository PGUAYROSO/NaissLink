from app.extensions import db
from domain.audit_log import AuditLog


class AuditRepository:

    @staticmethod
    def enregistrer(
        utilisateur: str,
        action: str,
        objet: str = None,
        adresse_ip: str = None
    ):

        log = AuditLog(
            utilisateur=utilisateur,
            action=action,
            objet=objet,
            adresse_ip=adresse_ip
        )

        db.session.add(log)
        db.session.commit()

        return log