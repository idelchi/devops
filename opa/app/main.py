"""Flask app to check user access to a resource. """

import argparse
import os

import requests
from flask import Flask, jsonify, request


def create_app(url: str) -> Flask:
    """Create a Flask app to check user access to a resource.

    Args:
        url (str): The URL of the OPA service.

    Returns:
        Flask: The Flask app.
    """
    app = Flask(__name__)

    @app.route("/api/user-access", methods=["POST"])
    def check_access():
        """Check if a user has access to a resource."""
        endpoint = "data/access/allow"

        data = request.get_json()
        username = data.get("Username")
        role = data.get("role")

        # Contact the OPA service to check if the user has access
        r = requests.post(f"{url}/{endpoint}", json={"input": {"username": username, "role": role}}, timeout=15)
        allowed = r.json()["result"]

        # Return the result to the user
        return jsonify(hasAccess=str(allowed))

    return app


if __name__ == "__main__":
    opa_url = os.environ.get("OPA_URL")

    parser = argparse.ArgumentParser(
        description="""Launches a Flask app to check user access to a resource.""",
        allow_abbrev=False,
    )

    parser.add_argument("--port", type=int, default=9999, required=False, help="Port to listen on.")
    parser.add_argument("--opa", type=str, default=opa_url, required=False, help="URL of the OPA service.")

    args = parser.parse_args()

    app = create_app(args.opa)

    context = ("cert.pem", "key.pem")  # certificate and key files

    app.run(host="0.0.0.0", port=args.port, debug=False, ssl_context=context)
