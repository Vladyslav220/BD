from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import parking_controller
from ..domain.parking import Parking

parking_bp = Blueprint('parking', __name__, url_prefix='/parking')


@parking_bp.route('', methods=['GET'])
def get_all_parkings() -> Response:
    """Отримати всі паркувальні місця."""
    parkings = parking_controller.find_all()
    return make_response(jsonify(parkings), HTTPStatus.OK)


@parking_bp.route('', methods=['POST'])
def create_parking() -> Response:
    """Створити нове паркувальне місце."""
    content = request.get_json()
    parking = Parking.create_from_dto(content)
    parking_controller.create(parking)
    return make_response(jsonify(parking.put_into_dto()), HTTPStatus.CREATED)


@parking_bp.route('/<int:parking_id>', methods=['GET'])
def get_parking(parking_id: int) -> Response:
    """Отримати паркувальне місце за ID."""
    parking = parking_controller.find_by_id(parking_id)
    if parking is None:
        return make_response({"error": "Паркувальне місце не знайдено"}, HTTPStatus.NOT_FOUND)
    return make_response(jsonify(parking), HTTPStatus.OK)


@parking_bp.route('/<int:parking_id>', methods=['PUT'])
def update_parking(parking_id: int) -> Response:
    """Оновити паркувальне місце за ID."""
    content = request.get_json()
    parking = Parking.create_from_dto(content)
    parking_controller.update(parking_id, parking)
    return make_response({"message": "Parking updated"}, HTTPStatus.OK)


@parking_bp.route('/<int:parking_id>', methods=['PATCH'])
def patch_parking(parking_id: int) -> Response:
    """Часткове оновлення паркувального місця за ID."""
    content = request.get_json()
    parking_controller.patch(parking_id, content)
    return make_response({"message": "Parking updated"}, HTTPStatus.OK)


@parking_bp.route('/<int:parking_id>', methods=['DELETE'])
def delete_parking(parking_id: int) -> Response:
    """Видалити паркувальне місце за ID."""
    parking_controller.delete(parking_id)
    return make_response({"message": "Parking deleted"}, HTTPStatus.OK)
