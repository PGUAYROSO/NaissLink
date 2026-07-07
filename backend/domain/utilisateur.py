from datetime import datetime, UTC

from app.extensions import db


class Utilisateur(db.Model):
    __tablename__ = "utilisateurs"

    id = db.Column(db.Integer, primary_key=True)

    nom = db.Column(
        db.String(100),
        nullable=False
    )

    prenom = db.Column(
        db.String(100),
        nullable=False
    )

    login = db.Column(
        db.String(50),
        unique=True,
        nullable=False
    )

    email = db.Column(
        db.String(150),
        unique=True,
        nullable=False
    )

    mot_de_passe = db.Column(
        db.String(255),
        nullable=False
    )

    role = db.Column(
        db.String(30),
        nullable=False
    )

    actif = db.Column(
        db.Boolean,
        default=True,
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
            "nom": self.nom,
            "prenom": self.prenom,
            "login": self.login,
            "email": self.email,
            "role": self.role,
            "actif": self.actif,
            "date_creation": (
                self.date_creation.isoformat()
                if self.date_creation else None
            )
        }