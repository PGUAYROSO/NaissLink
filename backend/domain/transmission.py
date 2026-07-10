from datetime import datetime, UTC
from enum import Enum

from app.extensions import db


class StatutTransmission(str, Enum):
    ENVOYEE = "ENVOYEE"
    RECEPTIONNEE = "RECEPTIONNEE"
    EN_INSTRUCTION = "EN_INSTRUCTION"
    COMPLEMENT_DEMANDE = "COMPLEMENT_DEMANDE"
    TRAITEE = "TRAITEE"
    ANNULEE = "ANNULEE"


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

    commune = db.Column(
        db.String(100),
        nullable=False
    )

    date_envoi = db.Column(
        db.DateTime,
        nullable=False,
        default=lambda: datetime.now(UTC)
    )

    expediteur = db.Column(
        db.String(100),
        nullable=False
    )

    statut = db.Column(
        db.String(30),
        nullable=False,
        default=StatutTransmission.ENVOYEE.value
    )

    commentaire = db.Column(
        db.Text
    )

    date_traitement = db.Column(
        db.DateTime
    )

    traite_par = db.Column(
        db.String(100)
    )

    dossier = db.relationship(
        "DossierDocumentaire",
        back_populates="transmissions"
    )

    # ------------------------
    # Méthodes métier
    # ------------------------

    def receptionner(self):
        self.statut = StatutTransmission.RECEPTIONNEE.value

    def mettre_en_instruction(self):
        self.statut = StatutTransmission.EN_INSTRUCTION.value

    def demander_complement(self, commentaire=None):
        self.statut = StatutTransmission.COMPLEMENT_DEMANDE.value

        if commentaire:
            self.commentaire = commentaire

    def traiter(self, utilisateur):
        self.statut = StatutTransmission.TRAITEE.value
        self.date_traitement = datetime.now(UTC)
        self.traite_par = utilisateur

    def annuler(self, commentaire=None):
        self.statut = StatutTransmission.ANNULEE.value

        if commentaire:
            self.commentaire = commentaire

    # ------------------------
    # Sérialisation
    # ------------------------

    def to_dict(self):

        return {

            "id": self.id,

            "dossier_id": self.dossier_id,

            "commune": self.commune,

            "expediteur": self.expediteur,

            "statut": self.statut,

            "commentaire": self.commentaire,

            "date_envoi": (
                self.date_envoi.isoformat()
                if self.date_envoi else None
            ),

            "date_traitement": (
                self.date_traitement.isoformat()
                if self.date_traitement else None
            ),

            "traite_par": self.traite_par
        }