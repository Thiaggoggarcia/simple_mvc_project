from flask import Blueprint, jsonify

person_routes_bp = Blueprint("person_routes", __name__)

@person_routes_bp.route("/person/create", methods=["POST"])
def create_person():
    return jsonify({"Hello":"World"}), 200