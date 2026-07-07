from infrastructure.document_repository import DocumentRepository


def executer(dossier_id):
    return DocumentRepository.trouver_par_dossier(dossier_id)