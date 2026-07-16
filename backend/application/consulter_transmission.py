from infrastructure.transmission_repository import TransmissionRepository


def executer(transmission_id):

    return TransmissionRepository.trouver_par_id(
        transmission_id
    )