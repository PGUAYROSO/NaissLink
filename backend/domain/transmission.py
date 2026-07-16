from datetime import datetime, UTC

from app.extensions import db


class Transmission(db.Model):
    __tablename__ = "transmissions"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    dossier_id = db.Column(
        db.Integer,
        db.ForeignKey("dossiers_documentaires.id"),
        nullable=False
    )
    dossier = db.relationship(
        "DossierDocumentaire",
        back_populates="transmissions"

    )

    destinataire = db.Column(
        db.String(255),
        nullable=False
    )

    mode = db.Column(
        db.String(50),
        nullable=False
    )

    statut = db.Column(
        db.String(30),
        nullable=False,
        default="EN_ATTENTE"
    )

    commentaire = db.Column(
        db.Text
    )

    cree_par = db.Column(
        db.String(100),
        nullable=False
    )

    date_creation = db.Column(
        db.DateTime,
        default=lambda: datetime.now(UTC),
        nullable=False
    )

    def to_dict(self):

        return {

            "id": self.id,

            "dossier_id": self.dossier_id,

            "destinataire": self.destinataire,

            "mode": self.mode,

            "statut": self.statut,

            "commentaire": self.commentaire,

            "cree_par": self.cree_par,

            "date_creation": (
                self.date_creation.isoformat()
                if self.date_creation else None
            )

        }