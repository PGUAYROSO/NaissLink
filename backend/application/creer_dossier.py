from infrastructure.dossier_repository import DossierRepository


def executer(numero_sejour: str):

    dossier = DossierRepository.trouver_par_numero_sejour(numero_sejour)

    if dossier:
        return None

    return DossierRepository.creer(numero_sejour)