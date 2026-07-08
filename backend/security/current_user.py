from flask_jwt_extended import (
    get_jwt,
    get_jwt_identity
)


def id():
    return int(get_jwt_identity())


def login():
    return get_jwt()["login"]


def role():
    return get_jwt()["role"]