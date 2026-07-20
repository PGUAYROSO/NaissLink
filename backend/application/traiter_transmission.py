from datetime import datetime, UTC

from app.extensions import db

from infrastructure.transmission_repository import (
    TransmissionRepository
)


def executer(
    transmission_id: int,
    utilisateur: str
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

    if not utilisateur:
        raise ValueError(
            "Le nom de l'utilisateur est obligatoire."
        )

    transmission.traiter()

    db.session.commit()

    return transmission