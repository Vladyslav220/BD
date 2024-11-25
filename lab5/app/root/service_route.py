from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import service_controller
from ..domain.service import Service
from ..insert import insert_record

service_bp = Blueprint('service', __name__, url_prefix='/service')


@service_bp.route('', methods=['GET'])
def get_all_services() -> Response:
    try:
        services = service_controller.find_all()
        return make_response(jsonify(services), HTTPStatus.OK)
    except Exception as e:
        # Логування помилки або додаткове оброблення
        return make_response(jsonify({"error": "An unexpected error occurred", "details": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)


@service_bp.route('', methods=['POST'])
def create_service() -> Response:
    content = request.get_json()
    if not content:
        return make_response(jsonify({"error": "Invalid input"}), HTTPStatus.BAD_REQUEST)

    try:
        service = Service.create_from_dto(content)
        service_controller.create(service)
        return make_response(jsonify(service.put_into_dto()), HTTPStatus.CREATED)
    except ValueError as e:
        # Якщо помилка валидації (наприклад, неправильний customer_id)
        return make_response(jsonify({"error": str(e)}), HTTPStatus.BAD_REQUEST)
    except Exception as e:
        # Загальний обробник для 500 помилок
        return make_response(jsonify({"error": "An unexpected error occurred", "details": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)


@service_bp.route('/<int:service_id>', methods=['GET'])
def get_service(service_id: int) -> Response:
    try:
        service = service_controller.find_by_id(service_id)
        if service is None:
            return make_response(jsonify({"error": "Service not found"}), HTTPStatus.NOT_FOUND)

        return make_response(jsonify(service.put_into_dto()), HTTPStatus.OK)
    except Exception as e:
        return make_response(jsonify({"error": "An unexpected error occurred", "details": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)


@service_bp.route('/<int:service_id>', methods=['PUT'])
def update_service(service_id: int) -> Response:
    content = request.get_json()
    if not content:
        return make_response(jsonify({"error": "Invalid input"}), HTTPStatus.BAD_REQUEST)

    try:
        service = Service.create_from_dto(content)
        if not service_controller.update(service_id, service):
            return make_response(jsonify({"error": "Service not found"}), HTTPStatus.NOT_FOUND)

        return make_response("Service updated", HTTPStatus.OK)
    except Exception as e:
        return make_response(jsonify({"error": "An unexpected error occurred", "details": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)


@service_bp.route('/<int:service_id>', methods=['PATCH'])
def patch_service(service_id: int) -> Response:
    content = request.get_json()
    if not content:
        return make_response(jsonify({"error": "Invalid input"}), HTTPStatus.BAD_REQUEST)

    try:
        if not service_controller.patch(service_id, content):
            return make_response(jsonify({"error": "Service not found"}), HTTPStatus.NOT_FOUND)

        return make_response("Service updated", HTTPStatus.OK)
    except Exception as e:
        return make_response(jsonify({"error": "An unexpected error occurred", "details": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)


@service_bp.route('/<int:service_id>', methods=['DELETE'])
def delete_service(service_id: int) -> Response:
    try:
        if not service_controller.delete(service_id):
            return make_response(jsonify({"error": "Service not found"}), HTTPStatus.NOT_FOUND)

        return make_response("Service deleted", HTTPStatus.OK)
    except Exception as e:
        return make_response(jsonify({"error": "An unexpected error occurred", "details": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)



@service_bp.route('/parametrized', methods=['POST'])
def insert_schedule_supplements_record():
    return insert_record(Service, request.get_json())