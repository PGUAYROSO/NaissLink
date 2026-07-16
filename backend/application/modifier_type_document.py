from infrastructure.type_document_repository import TypeDocumentRepository


def executer(
    type_document_id: int,
    code: str,
    libelle: str,
    description: str,
    ordre: int,
    actif: bool
):

    type_document = TypeDocumentRepository.trouver_par_id(
        type_document_id
    )

    if type_document is None:
        return None

    type_document.code = code
    type_document.libelle = libelle
    type_document.description = description
    type_document.ordre = ordre
    type_document.actif = actif

    return TypeDocumentRepository.modifier(
        type_document
    )