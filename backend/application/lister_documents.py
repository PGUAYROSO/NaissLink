from infrastructure.document_repository import DocumentRepository
from infrastructure.dossier_repository import DossierRepository


def executer(dossier_id):
    """
    Retourne la liste des documents d'un dossier documentaire.
    """

    dossier = DossierRepository.trouver_par_id(dossier_id)

    if dossier is None:
        raise ValueError("Dossier introuvable")

    return DocumentRepository.trouver_par_dossier(dossier_id)