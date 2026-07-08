from infrastructure.dossier_repository import DossierRepository


def executer(
    numero_sejour: str,
    cree_par: str
):

    dossier = DossierRepository.trouver_par_numero_sejour(numero_sejour)

    if dossier:
        return None

    return DossierRepository.creer(
        numero_sejour=numero_sejour,
        cree_par=cree_par
    )