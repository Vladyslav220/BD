from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import customer_controller
from ..domain.customer import Customer, create_dynamic_customer_tables
from ..insert import insert_record

customer_bp = Blueprint('customer', __name__, url_prefix='/customer')

@customer_bp.route('', methods=['GET'])
def get_all_customers() -> Response:
    customers = customer_controller.find_all()
    return make_response(jsonify(customers), HTTPStatus.OK)

@customer_bp.route('', methods=['POST'])
def create_customer() -> Response:
    content = request.get_json()
    if not content:  # Перевірка наявності вмісту
        return make_response("Invalid data", HTTPStatus.BAD_REQUEST)

    customer = Customer.create_from_dto(content)
    customer_controller.create(customer)
    return make_response(jsonify(customer.put_into_dto()), HTTPStatus.CREATED)

@customer_bp.route('/<int:customer_id>', methods=['GET'])
def get_customer(customer_id: int) -> Response:
    customer = customer_controller.find_by_id(customer_id)
    if customer is None:
        return make_response("Customer not found", HTTPStatus.NOT_FOUND)
    return make_response(jsonify(customer), HTTPStatus.OK)

@customer_bp.route('/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id: int) -> Response:
    content = request.get_json()
    if not content:
        return make_response("Invalid data", HTTPStatus.BAD_REQUEST)

    customer = Customer.create_from_dto(content)
    customer_controller.update(customer_id, customer)
    return make_response("Customer updated", HTTPStatus.OK)

@customer_bp.route('/<int:customer_id>', methods=['PATCH'])
def patch_customer(customer_id: int) -> Response:
    content = request.get_json()
    if not content:
        return make_response("Invalid data", HTTPStatus.BAD_REQUEST)

    customer_controller.patch(customer_id, content)
    return make_response("Customer updated", HTTPStatus.OK)

@customer_bp.route('/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id: int) -> Response:
    try:
        customer_controller.delete(customer_id)
        return make_response("Customer deleted", HTTPStatus.NO_CONTENT)
    except Exception as e:
        return make_response(str(e), HTTPStatus.CONFLICT)


@customer_bp.route('/create_dynamic_tables', methods=['POST'])
def create_tables_endpoint():
    table_names = create_dynamic_customer_tables()
    if isinstance(table_names, str):
        return jsonify({"error": table_names}), 404
    return jsonify({"message": f"Tables {', '.join(table_names)} created successfully!"}), 201


@customer_bp.route('/parametrized', methods=['POST'])
def insert_schedule_supplements_record():
    return insert_record(Customer, request.get_json())