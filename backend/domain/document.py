from datetime import datetime, UTC

from app.extensions import db


class Document(db.Model):
    __tablename__ = "documents"

    id = db.Column(db.Integer, primary_key=True)

    dossier_id = db.Column(
        db.Integer,
        db.ForeignKey("dossiers_documentaires.id"),
        nullable=False
    )

    nom = db.Column(
        db.String(255),
        nullable=False
    )

    type_document = db.Column(
        db.String(50),
        nullable=False
    )

    chemin_fichier = db.Column(
        db.String(500),
        nullable=False
    )

    taille = db.Column(db.Integer)

    date_upload = db.Column(
        db.DateTime,
        default=lambda: datetime.now(UTC),
        nullable=False
    )