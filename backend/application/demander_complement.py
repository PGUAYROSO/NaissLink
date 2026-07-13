from app.extensions import db

from infrastructure.transmission_repository import (
    TransmissionRepository
)


def executer(
    transmission_id: int,
    commentaire: str
):

    transmission = (
        TransmissionRepository.trouver_par_id(
            transmission_id
        )
    )

    if transmission is None:
        raise ValueError(
            "Transmission introuvable."
        )

    if not commentaire:
        raise ValueError(
            "Le commentaire est obligatoire."
        )

    transmission.demander_complement(commentaire)

    db.session.commit()

    return transmission