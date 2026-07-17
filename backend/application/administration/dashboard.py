from infrastructure.administration_repository import AdministrationRepository


def executer():

    return {

        "compteurs": {

            "utilisateurs":
                AdministrationRepository.compter_utilisateurs(),

            "dossiers":
                AdministrationRepository.compter_dossiers(),

            "documents":
                AdministrationRepository.compter_documents(),

            "transmissions":
                AdministrationRepository.compter_transmissions(),

            "types_documents":
                AdministrationRepository.compter_types_documents(),

            "audit_logs":
                AdministrationRepository.compter_audit_logs(),

        },

        "activite": [

            audit.to_dict()

            for audit in
            AdministrationRepository.derniers_audits()

        ]

    }