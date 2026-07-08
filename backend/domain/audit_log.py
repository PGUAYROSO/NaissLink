from datetime import datetime, UTC

from app.extensions import db


class AuditLog(db.Model):
    __tablename__ = "audit_logs"

    id = db.Column(db.Integer, primary_key=True)

    utilisateur = db.Column(
        db.String(100),
        nullable=False
    )

    action = db.Column(
        db.String(100),
        nullable=False
    )

    objet = db.Column(
        db.String(255)
    )

    adresse_ip = db.Column(
        db.String(45)
    )

    date_action = db.Column(
        db.DateTime,
        nullable=False,
        default=lambda: datetime.now(UTC)
    )

    def to_dict(self):
        return {
            "id": self.id,
            "utilisateur": self.utilisateur,
            "action": self.action,
            "objet": self.objet,
            "adresse_ip": self.adresse_ip,
            "date_action": (
                self.date_action.isoformat()
                if self.date_action else None
            )
        }