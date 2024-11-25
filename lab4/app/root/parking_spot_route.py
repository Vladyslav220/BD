from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import parking_spot_controller
from ..domain.parking_spot import ParkingSpot

parking_spot_bp = Blueprint('parking_spot', __name__, url_prefix='/parking_spot')


@parking_spot_bp.route('', methods=['GET'])
def get_all_parking_spots() -> Response:
    """Отримати всі паркувальні місця."""
    parking_spots = parking_spot_controller.find_all()
    return make_response(jsonify(parking_spots), HTTPStatus.OK)


@parking_spot_bp.route('', methods=['POST'])
def create_parking_spot() -> Response:
    """Створити нове паркувальне місце."""
    content = request.get_json()
    parking_spot = ParkingSpot.create_from_dto(content)
    parking_spot_controller.create(parking_spot)
    return make_response(jsonify(parking_spot.put_into_dto()), HTTPStatus.CREATED)


@parking_spot_bp.route('/<int:spot_id>', methods=['GET'])
def get_parking_spot(spot_id: int) -> Response:
    """Отримати паркувальне місце за ID."""
    parking_spot = parking_spot_controller.find_by_id(spot_id)
    if parking_spot is None:
        return make_response({"error": "Паркувальне місце не знайдено"}, HTTPStatus.NOT_FOUND)
    return make_response(jsonify(parking_spot), HTTPStatus.OK)


@parking_spot_bp.route('/<int:spot_id>', methods=['PUT'])
def update_parking_spot(spot_id: int) -> Response:
    """Оновити паркувальне місце за ID."""
    content = request.get_json()
    parking_spot = ParkingSpot.create_from_dto(content)
    parking_spot_controller.update(spot_id, parking_spot)
    return make_response({"message": "Parking spot updated"}, HTTPStatus.OK)


@parking_spot_bp.route('/<int:spot_id>', methods=['PATCH'])
def patch_parking_spot(spot_id: int) -> Response:
    """Часткове оновлення паркувального місця за ID."""
    content = request.get_json()
    parking_spot_controller.patch(spot_id, content)
    return make_response({"message": "Parking spot updated"}, HTTPStatus.OK)


@parking_spot_bp.route('/<int:spot_id>', methods=['DELETE'])
def delete_parking_spot(spot_id: int) -> Response:
    """Видалити паркувальне місце за ID."""
    parking_spot_controller.delete(spot_id)
    return make_response({"message": "Parking spot deleted"}, HTTPStatus.OK)
