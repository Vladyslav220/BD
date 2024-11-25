from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import payment_controller
from ..domain.payment import Payment
from ..insert import insert_record

payment_bp = Blueprint('payment', __name__, url_prefix='/payment')


@payment_bp.route('', methods=['GET'])
def get_all_payments() -> Response:
    """Отримати всі платежі."""
    payments = payment_controller.find_all()
    return make_response(jsonify(payments), HTTPStatus.OK)


@payment_bp.route('', methods=['POST'])
def create_payment() -> Response:
    """Створити новий платіж."""
    content = request.get_json()
    payment = Payment.create_from_dto(content)
    payment_controller.create(payment)
    return make_response(jsonify(payment.put_into_dto()), HTTPStatus.CREATED)


@payment_bp.route('/<int:payment_id>', methods=['GET'])
def get_payment(payment_id: int) -> Response:
    """Отримати платіж за ID."""
    payment = payment_controller.find_by_id(payment_id)
    if payment is None:
        return make_response({"error": "Платіж не знайдено"}, HTTPStatus.NOT_FOUND)
    return make_response(jsonify(payment), HTTPStatus.OK)


@payment_bp.route('/<int:payment_id>', methods=['PUT'])
def update_payment(payment_id: int) -> Response:
    """Оновити платіж за ID."""
    content = request.get_json()
    payment = Payment.create_from_dto(content)
    payment_controller.update(payment_id, payment)
    return make_response({"message": "Payment updated"}, HTTPStatus.OK)


@payment_bp.route('/<int:payment_id>', methods=['PATCH'])
def patch_payment(payment_id: int) -> Response:
    """Часткове оновлення платежу за ID."""
    content = request.get_json()
    payment_controller.patch(payment_id, content)
    return make_response({"message": "Payment updated"}, HTTPStatus.OK)


@payment_bp.route('/<int:payment_id>', methods=['DELETE'])
def delete_payment(payment_id: int) -> Response:
    """Видалити платіж за ID."""
    payment_controller.delete(payment_id)
    return make_response({"message": "Payment deleted"}, HTTPStatus.OK)


@payment_bp.route('/statistics', methods=['GET'])
def get_payment_statistics() -> Response:
    # Отримуємо параметри з запиту
    operation = request.args.get('operation', type=str)

    if operation not in ['max', 'min', 'sum', 'avg']:
        return make_response({"error": "Invalid operation"}, HTTPStatus.BAD_REQUEST)

    try:
        result = Payment.calculate_column(operation, 'amount')
        return make_response(jsonify({"operation": operation, "result": result}), HTTPStatus.OK)
    except ValueError as e:
        return make_response({"error": str(e)}, HTTPStatus.BAD_REQUEST)


@payment_bp.route('/parametrized', methods=['POST'])
def insert_schedule_supplements_record():
    return insert_record(Payment, request.get_json())