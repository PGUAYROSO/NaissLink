from domain.transmission import Transmission
from infrastructure.dossier_repository import DossierRepository
from infrastructure.transmission_repository import TransmissionRepository


def executer(
    numero_sejour,
    destinataire,
    mode,
    commentaire,
    cree_par
):

    dossier = DossierRepository.trouver_par_numero_sejour(
        numero_sejour
    )

    if dossier is None:
        raise ValueError(
            "Le dossier documentaire est introuvable."
        )

    transmission = Transmission(

        dossier_id=dossier.id,

        destinataire=destinataire,

        mode=mode,

        commentaire=commentaire,

        cree_par=cree_par,

        statut="EN_ATTENTE"

    )

    return TransmissionRepository.creer(
        transmission
    )