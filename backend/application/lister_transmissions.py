from infrastructure.transmission_repository import TransmissionRepository


def executer(dossier_id):

    return TransmissionRepository.lister_par_dossier(
        dossier_id
    )