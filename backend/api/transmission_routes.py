from flask import Blueprint, request, jsonify

from application.creer_transmission import executer


transmissions = Blueprint(
    "transmissions",
    __name__
)


@transmissions.route(
    "/transmissions",
    methods=["POST"]
)
def creer_transmission():

    try:

        data = request.get_json()

        transmission = executer(

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

        return jsonify({

            "message": str(e)

        }), 400

    except Exception as e:

        return jsonify({

            "message": "Erreur interne.",

            "erreur": str(e)

        }), 500