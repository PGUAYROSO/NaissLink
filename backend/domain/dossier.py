from datetime import datetime, UTC
from enum import Enum

from app.extensions import db


class StatutDossier(str, Enum):
    BROUILLON = "BROUILLON"
    EN_PREPARATION = "EN_PREPARATION"
    PRET_A_TRANSMETTRE = "PRET_A_TRANSMETTRE"
    TRANSMIS = "TRANSMIS"
    EN_INSTRUCTION = "EN_INSTRUCTION"
    COMPLEMENT_DEMANDE = "COMPLEMENT_DEMANDE"
    TRAITE = "TRAITE"
    ARCHIVE = "ARCHIVE"
    ANNULE = "ANNULE"


class DossierDocumentaire(db.Model):
    __tablename__ = "dossiers_documentaires"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

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
        db.String(30),
        nullable=False,
        default=StatutDossier.BROUILLON.value
    )

    cree_par = db.Column(
        db.String(100)
    )

    commentaire = db.Column(
        db.Text
    )

    archive = db.Column(
        db.Boolean,
        nullable=False,
        default=False
    )

    date_cloture = db.Column(
        db.DateTime
    )

    # -----------------------
    # Relations
    # -----------------------

    documents = db.relationship(
        "Document",
        backref="dossier",
        lazy=True,
        cascade="all, delete-orphan"
    )

    transmissions = db.relationship(
        "Transmission",
        back_populates="dossier",
        lazy=True,
        cascade="all, delete-orphan"
    )

    # -----------------------
    # Méthodes métier
    # -----------------------

    def est_complet(self):
        """
        Pour l'instant :
        un dossier est complet s'il contient
        au moins un document.

        Cette méthode sera améliorée lorsque
        nous gérerons les pièces obligatoires.
        """
        return len(self.documents) > 0

    def preparer(self):
        self.statut = StatutDossier.EN_PREPARATION.value

    def pret_a_transmettre(self):

        if not self.est_complet():
            raise ValueError(
                "Le dossier est incomplet."
            )

        self.statut = (
            StatutDossier.PRET_A_TRANSMETTRE.value
        )

    def transmettre(self):

        if self.statut != StatutDossier.PRET_A_TRANSMETTRE.value:
            raise ValueError(
                "Le dossier n'est pas prêt à être transmis."
            )

        self.statut = (
            StatutDossier.TRANSMIS.value
        )

    def mettre_en_instruction(self):

        self.statut = (
            StatutDossier.EN_INSTRUCTION.value
        )

    def demander_complement(self):

        self.statut = (
            StatutDossier.COMPLEMENT_DEMANDE.value
        )

    def traiter(self):

        self.statut = (
            StatutDossier.TRAITE.value
        )

    def archiver(self):

        self.archive = True

        self.date_cloture = datetime.now(UTC)

        self.statut = (
            StatutDossier.ARCHIVE.value
        )

    def annuler(self):

        self.statut = (
            StatutDossier.ANNULE.value
        )

    # -----------------------
    # Sérialisation
    # -----------------------

    def to_dict(self):

        return {

            "id": self.id,

            "numero_sejour": self.numero_sejour,

            "statut": (
                self.statut.value
                if hasattr(self.statut, "value")
                else self.statut
),

            "cree_par": self.cree_par,

            "commentaire": self.commentaire,

            "archive": self.archive,

            "nombre_documents": len(self.documents),

            "nombre_transmissions": len(self.transmissions),

            "date_creation": (
                self.date_creation.isoformat()
                if self.date_creation
                else None
            ),

            "date_cloture": (
                self.date_cloture.isoformat()
                if self.date_cloture
                else None
            )
        }