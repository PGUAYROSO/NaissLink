from infrastructure.type_document_repository import TypeDocumentRepository


def executer(type_document_id: int):

    type_document = TypeDocumentRepository.trouver_par_id(
        type_document_id
    )

    if type_document is None:
        return False

    TypeDocumentRepository.supprimer(
        type_document
    )

    return True