from infrastructure.historique_transmission_repository import (
    HistoriqueTransmissionRepository
)


def executer(transmission_id):

    historique = (
        HistoriqueTransmissionRepository
        .lister_par_transmission(
            transmission_id
        )
    )

    return [
        ligne.to_dict()
        for ligne in historique
    ]