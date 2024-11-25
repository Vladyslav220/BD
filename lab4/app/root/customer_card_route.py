from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import customer_card_controller
from ..domain.customer_card import CustomerCard

customer_card_bp = Blueprint('customer_card', __name__, url_prefix='/customer_card')


# Отримання всіх карток
@customer_card_bp.route('', methods=['GET'])
def get_all_customer_cards() -> Response:
    try:
        cards = customer_card_controller.find_all()
        return make_response(jsonify(cards), HTTPStatus.OK)
    except Exception as e:
        return make_response({"error": str(e)}, HTTPStatus.INTERNAL_SERVER_ERROR)


# Створення нової картки
@customer_card_bp.route('', methods=['POST'])
def create_customer_card() -> Response:
    content = request.get_json()

    # Валідація вхідних даних
    if not content or 'field_name' not in content:  # Змініть 'field_name' на потрібне поле
        return make_response({"error": "Invalid input"}, HTTPStatus.BAD_REQUEST)

    try:
        customer_card = CustomerCard.create_from_dto(content)
        customer_card_controller.create(customer_card)
        return make_response(jsonify(customer_card.put_into_dto()), HTTPStatus.CREATED)
    except Exception as e:
        return make_response({"error": str(e)}, HTTPStatus.BAD_REQUEST)


# Отримання картки за ID
@customer_card_bp.route('/<int:card_id>', methods=['GET'])
def get_customer_card(card_id: int) -> Response:
    try:
        card = customer_card_controller.find_by_id(card_id)
        if card is None:
            return make_response({"error": "Card not found"}, HTTPStatus.NOT_FOUND)
        return make_response(jsonify(card), HTTPStatus.OK)
    except Exception as e:
        return make_response({"error": str(e)}, HTTPStatus.INTERNAL_SERVER_ERROR)


# Оновлення картки
@customer_card_bp.route('/<int:card_id>', methods=['PUT'])
def update_customer_card(card_id: int) -> Response:
    content = request.get_json()

    # Валідація вхідних даних
    if not content or 'field_name' not in content:  # Змініть 'field_name' на потрібне поле
        return make_response({"error": "Invalid input"}, HTTPStatus.BAD_REQUEST)

    try:
        customer_card = CustomerCard.create_from_dto(content)
        customer_card_controller.update(card_id, customer_card)
        return make_response("Customer card updated", HTTPStatus.OK)
    except Exception as e:
        return make_response({"error": str(e)}, HTTPStatus.INTERNAL_SERVER_ERROR)


# Часткове оновлення картки
@customer_card_bp.route('/<int:card_id>', methods=['PATCH'])
def patch_customer_card(card_id: int) -> Response:
    content = request.get_json()
    try:
        customer_card_controller.patch(card_id, content)
        return make_response("Customer card updated", HTTPStatus.OK)
    except Exception as e:
        return make_response({"error": str(e)}, HTTPStatus.INTERNAL_SERVER_ERROR)


# Видалення картки
@customer_card_bp.route('/<int:card_id>', methods=['DELETE'])
def delete_customer_card(card_id: int) -> Response:
    try:
        customer_card_controller.delete(card_id)
        return make_response("Customer card deleted", HTTPStatus.OK)
    except Exception as e:
        return make_response({"error": str(e)}, HTTPStatus.INTERNAL_SERVER_ERROR)
