from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import company_controller
from ..domain.company import Company

company_bp = Blueprint('company', __name__, url_prefix='/company')


@company_bp.route('', methods=['GET'])
def get_all_companies() -> Response:
    companies = company_controller.find_all()
    return make_response(jsonify(companies), HTTPStatus.OK)


@company_bp.route('', methods=['POST'])
def create_company() -> Response:
    content = request.get_json()
    if not content:
        return make_response(jsonify({"error": "Invalid input"}), HTTPStatus.BAD_REQUEST)

    company = Company.create_from_dto(content)
    company_controller.create(company)
    return make_response(jsonify(company.put_into_dto()), HTTPStatus.CREATED)


@company_bp.route('/<int:company_id>', methods=['GET'])
def get_company(company_id: int) -> Response:
    company = company_controller.find_by_id(company_id)
    if company is None:
        return make_response(jsonify({"error": "Company not found"}), HTTPStatus.NOT_FOUND)

    return make_response(jsonify(company), HTTPStatus.OK)


@company_bp.route('/<int:company_id>', methods=['PUT'])
def update_company(company_id: int) -> Response:
    content = request.get_json()
    if not content:
        return make_response(jsonify({"error": "Invalid input"}), HTTPStatus.BAD_REQUEST)

    company = Company.create_from_dto(content)
    if not company_controller.update(company_id, company):
        return make_response(jsonify({"error": "Company not found"}), HTTPStatus.NOT_FOUND)

    return make_response("Company updated", HTTPStatus.OK)


@company_bp.route('/<int:company_id>', methods=['PATCH'])
def patch_company(company_id: int) -> Response:
    content = request.get_json()
    if not content:
        return make_response(jsonify({"error": "Invalid input"}), HTTPStatus.BAD_REQUEST)

    if not company_controller.patch(company_id, content):
        return make_response(jsonify({"error": "Company not found"}), HTTPStatus.NOT_FOUND)

    return make_response("Company updated", HTTPStatus.OK)


@company_bp.route('/<int:company_id>', methods=['DELETE'])
def delete_company(company_id: int) -> Response:
    if not company_controller.delete(company_id):
        return make_response(jsonify({"error": "Company not found"}), HTTPStatus.NOT_FOUND)

    return make_response("Company deleted", HTTPStatus.OK)
