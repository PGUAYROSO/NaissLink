from infrastructure.utilisateur_repository import UtilisateurRepository


def executer(
    utilisateur_id: int,
    actif: bool
):

    utilisateur = UtilisateurRepository.trouver_par_id(
        utilisateur_id
    )

    if utilisateur is None:
        return None

    # --------------------------------------------------------
    # Règle métier :
    # Impossible de désactiver le dernier administrateur actif
    # --------------------------------------------------------

    if (
        utilisateur.role == "ADMINISTRATEUR"
        and utilisateur.actif
        and not actif
    ):

        nb_admins = (
            UtilisateurRepository
            .compter_administrateurs_actifs()
        )

        if nb_admins <= 1:

            raise ValueError(
                "Impossible de désactiver le dernier administrateur actif."
            )

    utilisateur.actif = actif

    UtilisateurRepository.enregistrer()

    return utilisateur