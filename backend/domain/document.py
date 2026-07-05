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

    type_document = db.Column(
        db.String(100),
        nullable=False
    )

    nom_fichier = db.Column(
        db.String(255),
        nullable=False
    )

    chemin_fichier = db.Column(
        db.String(500),
        nullable=False
    )

    date_depot = db.Column(
        db.DateTime,
        default=lambda: datetime.now(UTC),
        nullable=False
    )

    statut = db.Column(
        db.String(30),
        default="DEPOSE",
        nullable=False
    )

    commentaire = db.Column(db.Text)

    def to_dict(self):
        return {
            "id": self.id,
            "dossier_id": self.dossier_id,
            "type_document": self.type_document,
            "nom_fichier": self.nom_fichier,
            "chemin_fichier": self.chemin_fichier,
            "date_depot": self.date_depot.isoformat(),
            "statut": self.statut,
            "commentaire": self.commentaire
        }