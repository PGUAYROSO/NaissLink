from infrastructure.utilisateur_repository import UtilisateurRepository
from security.permissions import ROLE_ADMIN


def executer(
    utilisateur_id: int,
    role: str
):

    utilisateur = UtilisateurRepository.trouver_par_id(
        utilisateur_id
    )

    if utilisateur is None:
        return None

    # --------------------------------------------------------
    # Règle métier :
    # Impossible de retirer le rôle du dernier administrateur
    # --------------------------------------------------------

    if (
        utilisateur.role == ROLE_ADMIN
        and role != ROLE_ADMIN
    ):

        nb_admins = (
            UtilisateurRepository
            .compter_par_role(ROLE_ADMIN)
        )

        if nb_admins <= 1:

            raise ValueError(
                "Impossible de modifier le rôle du dernier administrateur."
            )

    utilisateur.role = role

    UtilisateurRepository.enregistrer()

    return utilisateur