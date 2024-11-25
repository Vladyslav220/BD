from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import occupancy_controller
from ..domain.occupancy import Occupancy

occupancy_bp = Blueprint('occupancy', __name__, url_prefix='/occupancy')


@occupancy_bp.route('', methods=['GET'])
def get_all_occupancies() -> Response:
    """Отримати всі записи про зайнятість."""
    occupancies = occupancy_controller.find_all()
    return make_response(jsonify(occupancies), HTTPStatus.OK)


@occupancy_bp.route('', methods=['POST'])
def create_occupancy() -> Response:
    """Створити новий запис про зайнятість."""
    content = request.get_json()
    occupancy = Occupancy.create_from_dto(content)
    occupancy_controller.create(occupancy)
    return make_response(jsonify(occupancy.put_into_dto()), HTTPStatus.CREATED)


@occupancy_bp.route('/<int:occupancy_id>', methods=['GET'])
def get_occupancy(occupancy_id: int) -> Response:
    """Отримати запис про зайнятість за ID."""
    occupancy = occupancy_controller.find_by_id(occupancy_id)
    if occupancy is None:
        return make_response({"error": "Об'єкт не знайдено"}, HTTPStatus.NOT_FOUND)
    return make_response(jsonify(occupancy), HTTPStatus.OK)


@occupancy_bp.route('/<int:occupancy_id>', methods=['PUT'])
def update_occupancy(occupancy_id: int) -> Response:
    """Оновити запис про зайнятість за ID."""
    content = request.get_json()
    occupancy = Occupancy.create_from_dto(content)
    occupancy_controller.update(occupancy_id, occupancy)
    return make_response({"message": "Occupancy updated"}, HTTPStatus.OK)


@occupancy_bp.route('/<int:occupancy_id>', methods=['PATCH'])
def patch_occupancy(occupancy_id: int) -> Response:
    """Часткове оновлення запису про зайнятість за ID."""
    content = request.get_json()
    occupancy_controller.patch(occupancy_id, content)
    return make_response({"message": "Occupancy updated"}, HTTPStatus.OK)


@occupancy_bp.route('/<int:occupancy_id>', methods=['DELETE'])
def delete_occupancy(occupancy_id: int) -> Response:
    """Видалити запис про зайнятість за ID."""
    occupancy_controller.delete(occupancy_id)
    return make_response({"message": "Occupancy deleted"}, HTTPStatus.OK)
