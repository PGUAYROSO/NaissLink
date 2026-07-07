from infrastructure.document_repository import DocumentRepository


def executer(document_id):
    return DocumentRepository.trouver_par_id(document_id)