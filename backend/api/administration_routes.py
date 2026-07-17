from flask import Blueprint, jsonify

from application.administration.dashboard import executer

administration = Blueprint(
    "administration",
    __name__
)


@administration.get("/administration/dashboard")
def dashboard():
    return jsonify(executer())