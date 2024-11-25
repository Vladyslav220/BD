from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import ticket_controller
from ..domain.ticket import Ticket
from ..insert import insert_record

ticket_bp = Blueprint('ticket', __name__, url_prefix='/ticket')


@ticket_bp.route('', methods=['GET'])
def get_all_tickets() -> Response:
    """Отримати всі квитки."""
    tickets = ticket_controller.find_all()
    return make_response(jsonify(tickets), HTTPStatus.OK)


@ticket_bp.route('', methods=['POST'])
def create_ticket() -> Response:
    """Створити новий квиток."""
    content = request.get_json()
    ticket = Ticket.create_from_dto(content)
    ticket_controller.create(ticket)
    return make_response(jsonify(ticket.put_into_dto()), HTTPStatus.CREATED)


@ticket_bp.route('/<int:ticket_id>', methods=['GET'])
def get_ticket(ticket_id: int) -> Response:
    """Отримати квиток за ID."""
    ticket = ticket_controller.find_by_id(ticket_id)
    if ticket is None:
        return make_response(jsonify({"error": "Квиток не знайдено"}), HTTPStatus.NOT_FOUND)
    return make_response(jsonify(ticket), HTTPStatus.OK)


@ticket_bp.route('/<int:ticket_id>', methods=['PUT'])
def update_ticket(ticket_id: int) -> Response:
    """Оновити квиток за ID."""
    content = request.get_json()
    ticket = Ticket.create_from_dto(content)

    # Перевірка наявності квитка
    existing_ticket = ticket_controller.find_by_id(ticket_id)
    if existing_ticket is None:
        return make_response(jsonify({"error": "Квиток не знайдено"}), HTTPStatus.NOT_FOUND)

    ticket_controller.update(ticket_id, ticket)
    return make_response(jsonify({"message": "Квиток оновлено"}), HTTPStatus.OK)


@ticket_bp.route('/<int:ticket_id>', methods=['PATCH'])
def patch_ticket(ticket_id: int) -> Response:
    """Часткове оновлення квитка за ID."""
    content = request.get_json()

    # Перевірка наявності квитка
    existing_ticket = ticket_controller.find_by_id(ticket_id)
    if existing_ticket is None:
        return make_response(jsonify({"error": "Квиток не знайдено"}), HTTPStatus.NOT_FOUND)

    ticket_controller.patch(ticket_id, content)
    return make_response(jsonify({"message": "Квиток оновлено"}), HTTPStatus.OK)


@ticket_bp.route('/<int:ticket_id>', methods=['DELETE'])
def delete_ticket(ticket_id: int) -> Response:
    """Видалити квиток за ID."""
    existing_ticket = ticket_controller.find_by_id(ticket_id)
    if existing_ticket is None:
        return make_response(jsonify({"error": "Квиток не знайдено"}), HTTPStatus.NOT_FOUND)

    ticket_controller.delete(ticket_id)
    return make_response(jsonify({"message": "Квиток видалено"}), HTTPStatus.OK)


@ticket_bp.route('/parametrized', methods=['POST'])
def insert_schedule_supplements_record():
    return insert_record(Ticket, request.get_json())