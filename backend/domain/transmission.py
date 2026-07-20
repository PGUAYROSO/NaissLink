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

            "numero_sejour": (
                self.dossier.numero_sejour
                if self.dossier else None
            ),

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
    def receptionner(self):

        if self.statut != "EN_ATTENTE":
            raise ValueError(
                "La transmission ne peut pas être réceptionnée."
            )

        self.statut = "RECEPTIONNEE"


    def mettre_en_instruction(self):

        if self.statut != "RECEPTIONNEE":
            raise ValueError(
                "La transmission doit être réceptionnée."
            )

        self.statut = "EN_INSTRUCTION"


    def demander_complement(self, commentaire):

        if self.statut != "EN_INSTRUCTION":
            raise ValueError(
                "La transmission doit être en instruction."
            )

        self.statut = "COMPLEMENT"
        self.commentaire = commentaire


    def traiter(self):

        if self.statut not in (
            "EN_INSTRUCTION",
            "COMPLEMENT"
        ):
            raise ValueError(
                "La transmission ne peut pas être traitée."
            )

        self.statut = "TRAITEE"