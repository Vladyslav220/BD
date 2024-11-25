from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import reservation_controller
from ..domain.reservation import Reservation

reservation_bp = Blueprint('reservation', __name__, url_prefix='/reservation')


@reservation_bp.route('', methods=['GET'])
def get_all_reservations() -> Response:
    """Отримати всі бронювання."""
    reservations = reservation_controller.find_all()
    return make_response(jsonify(reservations), HTTPStatus.OK)


@reservation_bp.route('', methods=['POST'])
def create_reservation() -> Response:
    """Створити нове бронювання."""
    content = request.get_json()
    reservation = Reservation.create_from_dto(content)
    reservation_controller.create(reservation)
    return make_response(jsonify(reservation.put_into_dto()), HTTPStatus.CREATED)


@reservation_bp.route('/<int:reservation_id>', methods=['GET'])
def get_reservation(reservation_id: int) -> Response:
    """Отримати бронювання за ID."""
    reservation = reservation_controller.find_by_id(reservation_id)
    if reservation is None:
        return make_response({"error": "Бронювання не знайдено"}, HTTPStatus.NOT_FOUND)
    return make_response(jsonify(reservation), HTTPStatus.OK)


@reservation_bp.route('/<int:reservation_id>', methods=['PUT'])
def update_reservation(reservation_id: int) -> Response:
    """Оновити бронювання за ID."""
    content = request.get_json()
    reservation = Reservation.create_from_dto(content)
    reservation_controller.update(reservation_id, reservation)
    return make_response({"message": "Бронювання оновлено"}, HTTPStatus.OK)


@reservation_bp.route('/<int:reservation_id>', methods=['PATCH'])
def patch_reservation(reservation_id: int) -> Response:
    """Часткове оновлення бронювання за ID."""
    content = request.get_json()
    reservation_controller.patch(reservation_id, content)
    return make_response({"message": "Бронювання оновлено"}, HTTPStatus.OK)


@reservation_bp.route('/<int:reservation_id>', methods=['DELETE'])
def delete_reservation(reservation_id: int) -> Response:
    """Видалити бронювання за ID."""
    reservation_controller.delete(reservation_id)
    return make_response({"message": "Бронювання видалено"}, HTTPStatus.OK)
