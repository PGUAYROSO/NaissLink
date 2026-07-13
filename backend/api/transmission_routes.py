from flask import Blueprint, request, jsonify

from application.creer_transmission import (
    executer as creer_transmission
)

from application.receptionner_transmission import (
    executer as receptionner_transmission
)

from application.mettre_en_instruction import (
    executer as mettre_en_instruction
)

from application.traiter_transmission import (
    executer as traiter_transmission
)

from application.demander_complement import (
    executer as demander_complement
)


transmissions = Blueprint(
    "transmissions",
    __name__
)


# ------------------------------------------------------------------
# Création d'une transmission
# ------------------------------------------------------------------

@transmissions.route(
    "/transmissions",
    methods=["POST"]
)
def creer():

    try:

        data = request.get_json()

        transmission = creer_transmission(

            dossier_id=data["dossier_id"],

            commune=data["commune"],

            expediteur=data["expediteur"],

            commentaire=data.get("commentaire")

        )

        return jsonify({

            "message": "Transmission créée avec succès.",

            "transmission": transmission.to_dict()

        }), 201

    except ValueError as e:

        return jsonify({"message": str(e)}), 400

    except Exception as e:

        return jsonify({
            "message": "Erreur interne.",
            "erreur": str(e)
        }), 500


# ------------------------------------------------------------------
# Réception par la mairie
# ------------------------------------------------------------------

@transmissions.route(
    "/transmissions/<int:id>/receptionner",
    methods=["PUT"]
)
def receptionner(id):

    try:

        transmission = receptionner_transmission(id)

        return jsonify({

            "message": "Transmission réceptionnée.",

            "transmission": transmission.to_dict()

        }), 200

    except ValueError as e:

        return jsonify({"message": str(e)}), 400

    except Exception as e:

        return jsonify({

            "message": "Erreur interne.",

            "erreur": str(e)

        }), 500


# ------------------------------------------------------------------
# Mise en instruction
# ------------------------------------------------------------------

@transmissions.route(
    "/transmissions/<int:id>/instruction",
    methods=["PUT"]
)
def instruction(id):

    try:

        transmission = mettre_en_instruction(id)

        return jsonify({

            "message": "Transmission mise en instruction.",

            "transmission": transmission.to_dict()

        }), 200

    except ValueError as e:

        return jsonify({"message": str(e)}), 400

    except Exception as e:

        return jsonify({

            "message": "Erreur interne.",

            "erreur": str(e)

        }), 500


# ------------------------------------------------------------------
# Traitement final
# ------------------------------------------------------------------

@transmissions.route(
    "/transmissions/<int:id>/traiter",
    methods=["PUT"]
)
def traiter(id):

    try:

        data = request.get_json() or {}

        utilisateur = data.get(
            "utilisateur",
            "Etat Civil"
        )

        transmission = traiter_transmission(
            id,
            utilisateur
        )

        return jsonify({

            "message": "Transmission traitée.",

            "transmission": transmission.to_dict()

        }), 200

    except ValueError as e:

        return jsonify({"message": str(e)}), 400

    except Exception as e:

        return jsonify({

            "message": "Erreur interne.",

            "erreur": str(e)

        }), 500

@transmissions.route(
    "/transmissions/<int:id>/complement",
    methods=["PUT"]
)
def complement(id):

    try:

        data = request.get_json()

        transmission = demander_complement(
            id,
            data["commentaire"]
        )

        return jsonify({

            "message": "Complément demandé.",

            "transmission": transmission.to_dict()

        }), 200

    except ValueError as e:

        return jsonify({
            "message": str(e)
        }), 400

    except Exception as e:

        return jsonify({

            "message": "Erreur interne.",

            "erreur": str(e)

        }), 500