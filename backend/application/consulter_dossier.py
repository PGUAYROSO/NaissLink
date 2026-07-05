from infrastructure.dossier_repository import DossierRepository


def executer(numero_sejour: str):
    return DossierRepository.trouver_par_numero_sejour(numero_sejour)