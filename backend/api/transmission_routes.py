from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity

from application.creer_transmission import (executer as creer_transmission)
from application.receptionner_transmission import (executer as receptionner_transmission)
from application.mettre_en_instruction import (executer as mettre_en_instruction)
from application.traiter_transmission import (executer as traiter_transmission)
from application.demander_complement import (executer as demander_complement)
from application.lister_toutes_transmissions import (executer as lister_toutes_transmissions)
from application.lister_historique_transmission import (executer as lister_historique)




transmissions = Blueprint("transmissions", __name__)


# ------------------------------------------------------------------
# Création d'une transmission
# ------------------------------------------------------------------

@transmissions.post("/transmissions")
@jwt_required()
def creer():

    try:

        data = request.get_json()

        utilisateur = get_jwt_identity()
        print(get_jwt_identity())
        transmission = creer_transmission(

            numero_sejour=data["numero_sejour"],

            destinataire=data["commune"],

            mode="NaissLink",

            commentaire=data.get("commentaire"),

            cree_par=utilisateur

        )

        return jsonify({

            "message": "Transmission créée avec succès.",

            "transmission": transmission.to_dict()

        }), 201

    except ValueError as e:

        return jsonify({"message": str(e)}), 400


    except Exception as e:

        import traceback

        traceback.print_exc()

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

        utilisateur = get_jwt_identity()

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

        utilisateur = get_jwt_identity()

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

        utilisateur = get_jwt_identity()

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

        utilisateur = get_jwt_identity()

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

# ------------------------------------------------------------------
# Lister historique
# ------------------------------------------------------------------

@transmissions.get("/transmissions/<int:transmission_id>/historique")
@jwt_required()
def historique(transmission_id):

    return jsonify(
        lister_historique(transmission_id)
    )