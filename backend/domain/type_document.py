from enum import Enum

from app.extensions import db


# ------------------------------------------------------------------
# Enum utilisé dans le code métier
# ------------------------------------------------------------------

class CodeTypeDocument(str, Enum):

    DECLARATION_NAISSANCE = "DECLARATION_NAISSANCE"

    CNI_MERE = "CNI_MERE"

    CNI_PERE = "CNI_PERE"

    LIVRET_FAMILLE = "LIVRET_FAMILLE"

    PASSEPORT = "PASSEPORT"

    RECONNAISSANCE_ANTICIPEE = "RECONNAISSANCE_ANTICIPEE"

    ACTE_MARIAGE = "ACTE_MARIAGE"

    JUGEMENT = "JUGEMENT"

    AUTRE = "AUTRE"


# ------------------------------------------------------------------
# Référentiel des types de documents
# ------------------------------------------------------------------

class TypeDocument(db.Model):
    __tablename__ = "types_documents"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    code = db.Column(
        db.String(50),
        unique=True,
        nullable=False
    )

    libelle = db.Column(
        db.String(150),
        nullable=False
    )

    description = db.Column(
        db.Text
    )

    ordre = db.Column(
        db.Integer,
        nullable=False,
        default=0
    )

    actif = db.Column(
        db.Boolean,
        nullable=False,
        default=True
    )

    # --------------------------------------------------------------
    # Sérialisation
    # --------------------------------------------------------------

    def to_dict(self):

        return {

            "id": self.id,

            "code": self.code,

            "libelle": self.libelle,

            "description": self.description,

            "ordre": self.ordre,

            "actif": self.actif

        }

    # --------------------------------------------------------------
    # Affichage
    # --------------------------------------------------------------

    def __repr__(self):

        return f"<TypeDocument {self.code}>"