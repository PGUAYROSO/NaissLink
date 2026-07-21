from datetime import datetime, UTC

from app.extensions import db


class HistoriqueTransmission(db.Model):
    __tablename__ = "historique_transmissions"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    transmission_id = db.Column(
        db.Integer,
        db.ForeignKey("transmissions.id"),
        nullable=False
    )

    transmission = db.relationship(
        "Transmission",
        back_populates="historique"
    )

    date_action = db.Column(
        db.DateTime,
        nullable=False,
        default=lambda: datetime.now(UTC)
    )

    utilisateur = db.Column(
        db.String(100),
        nullable=False
    )

    action = db.Column(
        db.String(100),
        nullable=False
    )

    commentaire = db.Column(
        db.Text,
        nullable=True
    )

    def to_dict(self):
        return {
            "id": self.id,
            "transmission_id": self.transmission_id,
            "date_action": self.date_action.isoformat(),
            "utilisateur": self.utilisateur,
            "action": self.action,
            "commentaire": self.commentaire
        }