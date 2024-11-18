from flask import Blueprint, jsonify, request
from src.view.http_types.http_request import HttpRequest

person_routes_bp = Blueprint("person_routes", __name__)

@person_routes_bp.route("/person/create", methods=["POST"])
def create_person():
    http_request = HttpRequest(body=request.json)
    # Mandar http_request para views
    return jsonify({"Hello":"World"}), 200

