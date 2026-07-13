from app.extensions import db

from infrastructure.transmission_repository import (
    TransmissionRepository
)


def executer(transmission_id: int):

    transmission = (
        TransmissionRepository.trouver_par_id(
            transmission_id
        )
    )

    if transmission is None:
        raise ValueError(
            "Transmission introuvable."
        )

    transmission.receptionner()

    db.session.commit()

    return transmission