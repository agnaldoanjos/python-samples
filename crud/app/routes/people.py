from flask import Blueprint, request, jsonify
from app.services import get_all_people, create_person, get_person, update_person, delete_person

people_bp = Blueprint('people', __name__)

@people_bp.route('/', methods=['GET'])
def get_all_people_route():
    return jsonify(get_all_people())

@people_bp.route('/', methods=['POST'])
def create_person_route():
    data = request.get_json()
    return jsonify(create_person(data)), 201

@people_bp.route('/<int:person_id>', methods=['GET'])
def get_person_route(person_id):
    return jsonify(get_person(person_id))

@people_bp.route('/<int:person_id>', methods=['PUT'])
def update_person_route(person_id):
    data = request.get_json()
    return jsonify(update_person(person_id, data))

@people_bp.route('/<int:person_id>', methods=['DELETE'])
def delete_person_route(person_id):
    return jsonify(delete_person(person_id))
