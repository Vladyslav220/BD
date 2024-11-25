from flask import Blueprint, jsonify, Response, request, make_response
from http import HTTPStatus
from ..domain.vehicle import Vehicle, insert_random_vehicles
from ..controller import vehicle_controller
from ..insert import insert_record

vehicle_bp = Blueprint('vehicle', __name__, url_prefix='/vehicle')


@vehicle_bp.route('', methods=['GET'])
def get_all_vehicles() -> Response:
    """Отримати всі транспортні засоби."""
    vehicles = vehicle_controller.find_all()
    return make_response(jsonify([vehicle.put_into_dto() for vehicle in vehicles]), HTTPStatus.OK)


@vehicle_bp.route('/<int:vehicle_id>', methods=['GET'])
def get_vehicle(vehicle_id: int) -> Response:
    """Отримати транспортний засіб за ID."""
    vehicle = vehicle_controller.find_by_id(vehicle_id)
    if vehicle is None:
        return make_response({"error": "Транспортний засіб не знайдено"}, HTTPStatus.NOT_FOUND)
    return make_response(jsonify(vehicle.put_into_dto()), HTTPStatus.OK)


@vehicle_bp.route('', methods=['POST'])
def create_vehicle() -> Response:
    """Створити новий транспортний засіб."""
    content = request.get_json()

    if 'plate_number' not in content or 'owner_id' not in content:
        return make_response({"error": "Необхідні поля: plate_number, owner_id"}, HTTPStatus.BAD_REQUEST)

    try:
        vehicle = Vehicle.create_from_dto(content)
        vehicle_controller.create(vehicle)
        return make_response(jsonify(vehicle.put_into_dto()), HTTPStatus.CREATED)
    except Exception as e:
        return make_response({"error": str(e)}, HTTPStatus.INTERNAL_SERVER_ERROR)


@vehicle_bp.route('/generate', methods=['POST'])
def generate_vehicles() -> Response:
    try:
        vehicles = insert_random_vehicles()
        return make_response(
            jsonify([vehicle.put_into_dto() for vehicle in vehicles]),
            HTTPStatus.CREATED
        )
    except Exception as e:
        return make_response({"error": str(e)}, HTTPStatus.INTERNAL_SERVER_ERROR)


@vehicle_bp.route('/<int:vehicle_id>', methods=['PUT'])
def update_vehicle(vehicle_id: int) -> Response:
    """Оновити транспортний засіб за ID."""
    content = request.get_json()

    if content is None:
        return make_response({"error": "Необхідні дані для оновлення відсутні"}, HTTPStatus.BAD_REQUEST)

    vehicle = vehicle_controller.find_by_id(vehicle_id)
    if vehicle is None:
        return make_response({"error": "Транспортний засіб не знайдено"}, HTTPStatus.NOT_FOUND)

    updated_vehicle = Vehicle.create_from_dto(content)
    vehicle_controller.update(vehicle_id, updated_vehicle)

    return make_response({"message": "Транспортний засіб оновлено"}, HTTPStatus.OK)


@vehicle_bp.route('/<int:vehicle_id>', methods=['PATCH'])
def patch_vehicle(vehicle_id: int) -> Response:
    """Часткове оновлення транспортного засобу за ID."""
    content = request.get_json()

    if content is None:
        return make_response({"error": "Необхідні дані для часткового оновлення відсутні"}, HTTPStatus.BAD_REQUEST)

    vehicle = vehicle_controller.find_by_id(vehicle_id)
    if vehicle is None:
        return make_response({"error": "Транспортний засіб не знайдено"}, HTTPStatus.NOT_FOUND)

    vehicle_controller.patch(vehicle_id, content)

    return make_response({"message": "Транспортний засіб частково оновлено"}, HTTPStatus.OK)


@vehicle_bp.route('/<int:vehicle_id>', methods=['DELETE'])
def delete_vehicle(vehicle_id: int) -> Response:
    """Видалити транспортний засіб за ID."""
    vehicle = vehicle_controller.find_by_id(vehicle_id)
    if vehicle is None:
        return make_response({"error": "Транспортний засіб не знайдено"}, HTTPStatus.NOT_FOUND)

    vehicle_controller.delete(vehicle_id)

    return make_response({"message": "Транспортний засіб видалено"}, HTTPStatus.OK)


@vehicle_bp.route('/parametrized', methods=['POST'])
def insert_schedule_supplements_record():
    return insert_record(Vehicle, request.get_json())