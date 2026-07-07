from datetime import datetime, UTC

from app.extensions import db


class DossierDocumentaire(db.Model):
    __tablename__ = "dossiers_documentaires"

    id = db.Column(db.Integer, primary_key=True)

    numero_sejour = db.Column(
        db.String(20),
        nullable=False,
        unique=True
    )

    date_creation = db.Column(
        db.DateTime,
        nullable=False,
        default=lambda: datetime.now(UTC)
    )

    statut = db.Column(
        db.String(20),
        nullable=False,
        default="BROUILLON"
    )

    cree_par = db.Column(db.String(100))

    commentaire = db.Column(db.Text)

    def to_dict(self):
        return {
            "id": self.id,
            "numero_sejour": self.numero_sejour,
            "statut": self.statut,
            "cree_par": self.cree_par,
            "commentaire": self.commentaire,
            "date_creation": self.date_creation.isoformat()
        }

    documents = db.relationship(
        "Document",
        backref="dossier",
        lazy=True,
        cascade="all, delete-orphan"
    )