from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import company_customer_controller
from ..domain.company_customer import CompanyCustomer
from ..insert import insert_record
company_customer_bp = Blueprint('company_customer', __name__, url_prefix='/company_customer')

# Отримання всіх зв'язків компаній і клієнтів
@company_customer_bp.route('', methods=['GET'])
def get_all_company_customers() -> Response:
    try:
        # Викликаємо метод контролера для отримання всіх зв'язків
        connections = company_customer_controller.find_all()
        return make_response(jsonify(connections), HTTPStatus.OK)
    except Exception as e:
        return make_response({"error": str(e)}, HTTPStatus.INTERNAL_SERVER_ERROR)


# Створення нового зв'язку між компанією та клієнтом
@company_customer_bp.route('', methods=['POST'])
def create_company_customer() -> Response:
    content = request.get_json()
    if not content or 'company_name' not in content or 'first_name' not in content:
        return make_response({"error": "Invalid input"}, HTTPStatus.BAD_REQUEST)
    try:
        company_customer = CompanyCustomer.add_customer_to_company(
            company_name=content['company_name'],
            first_name=content['first_name']
        )
        return make_response(jsonify(company_customer.put_into_dto()), HTTPStatus.CREATED)
    except ValueError as e:
        return make_response({"error": str(e)}, HTTPStatus.BAD_REQUEST)
    except Exception as e:
        return make_response({"error": str(e)}, HTTPStatus.INTERNAL_SERVER_ERROR)


# Отримання зв'язку між компанією та клієнтом
@company_customer_bp.route('/<int:company_id>/<int:customer_id>', methods=['GET'])
def get_company_customer(company_id: int, customer_id: int) -> Response:
    try:
        # Шукаємо конкретний зв'язок за company_id та customer_id
        connection = company_customer_controller.find_by_ids(company_id, customer_id)
        if connection is None:
            return make_response({"error": "Connection not found"}, HTTPStatus.NOT_FOUND)
        return make_response(jsonify(connection), HTTPStatus.OK)
    except Exception as e:
        return make_response({"error": str(e)}, HTTPStatus.INTERNAL_SERVER_ERROR)


# Оновлення зв'язку між компанією та клієнтом
@company_customer_bp.route('/<int:company_id>/<int:customer_id>', methods=['PUT'])
def update_company_customer(company_id: int, customer_id: int) -> Response:
    content = request.get_json()

    # Валідація вхідних даних
    if not content:
        return make_response({"error": "Invalid input"}, HTTPStatus.BAD_REQUEST)

    try:
        # Створення об'єкта компанії та клієнта з переданих даних
        company_customer = CompanyCustomer.create_from_dto(content)
        company_customer_controller.update((company_id, customer_id), company_customer)
        return make_response("Company-customer connection updated", HTTPStatus.OK)
    except Exception as e:
        return make_response({"error": str(e)}, HTTPStatus.INTERNAL_SERVER_ERROR)


# Часткове оновлення зв'язку між компанією та клієнтом
@company_customer_bp.route('/<int:company_id>/<int:customer_id>', methods=['PATCH'])
def patch_company_customer(company_id: int, customer_id: int) -> Response:
    content = request.get_json()
    try:
        company_customer_controller.patch((company_id, customer_id), content)
        return make_response("Company-customer connection updated", HTTPStatus.OK)
    except Exception as e:
        return make_response({"error": str(e)}, HTTPStatus.INTERNAL_SERVER_ERROR)


# Видалення зв'язку між компанією та клієнтом
@company_customer_bp.route('/<int:company_id>/<int:customer_id>', methods=['DELETE'])
def delete_company_customer(company_id: int, customer_id: int) -> Response:
    try:
        company_customer_controller.delete((company_id, customer_id))
        return make_response("Company-customer connection deleted", HTTPStatus.OK)
    except Exception as e:
        return make_response({"error": str(e)}, HTTPStatus.INTERNAL_SERVER_ERROR)

@company_customer_bp.route('/parametrized', methods=['POST'])
def insert_schedule_supplements_record():
    return insert_record(CompanyCustomer, request.get_json())
