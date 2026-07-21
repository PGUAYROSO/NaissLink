from app.extensions import db

from infrastructure.transmission_repository import (
    TransmissionRepository
)

from application.ajouter_historique_transmission import (
    executer as ajouter_historique
)


def executer(
    transmission_id,
    utilisateur="Mairie"
):

    try:

        transmission = TransmissionRepository.trouver_par_id(
            transmission_id
        )

        if transmission is None:
            raise ValueError(
                "Transmission introuvable."
            )

        transmission.traiter()

        ajouter_historique(

            transmission_id=transmission.id,

            utilisateur=utilisateur,

            action="Transmission traitée"

        )

        db.session.commit()

        return transmission

    except Exception:

        db.session.rollback()

        raise