from functools import wraps

from flask import jsonify

from security.current_user import role


def roles_required(*roles):

    def decorator(f):

        @wraps(f)
        def wrapper(*args, **kwargs):

            if role() not in roles:

                return jsonify({
                    "message": "Accès refusé."
                }), 403

            return f(*args, **kwargs)

        return wrapper

    return decorator