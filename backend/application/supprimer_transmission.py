from infrastructure.transmission_repository import TransmissionRepository


def executer(transmission):

    TransmissionRepository.supprimer(
        transmission
    )