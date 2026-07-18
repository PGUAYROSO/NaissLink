from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from application.creer_transmission import (executer as creer_transmission)

from application.receptionner_transmission import (executer as receptionner_transmission)

from application.mettre_en_instruction import (executer as mettre_en_instruction)

from application.traiter_transmission import (executer as traiter_transmission)

from application.demander_complement import (executer as demander_complement)

from application.lister_toutes_transmissions import (executer as lister_toutes_transmissions)




transmissions = Blueprint("transmissions", __name__)


# ------------------------------------------------------------------
# Création d'une transmission
# ------------------------------------------------------------------

@transmissions.post("/transmissions")
@jwt_required()
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

@transmissions.put("/transmissions/<int:id>/receptionner",)
@jwt_required()
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

@transmissions.put("/transmissions/<int:id>/instruction",)
@jwt_required()
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

@transmissions.put("/transmissions/<int:id>/traiter",)
@jwt_required()
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

@transmissions.put("/transmissions/<int:id>/complement",)
@jwt_required()
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

# ------------------------------------------------------------------
# Liste des transmissions
# ------------------------------------------------------------------

@transmissions.get("/transmissions")
@jwt_required()
def liste():

    transmissions_liste = lister_toutes_transmissions()

    return jsonify([
        transmission.to_dict()
        for transmission in transmissions_liste
    ])