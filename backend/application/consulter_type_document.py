from infrastructure.type_document_repository import TypeDocumentRepository


def executer(type_document_id: int):

    return TypeDocumentRepository.trouver_par_id(
        type_document_id
    )