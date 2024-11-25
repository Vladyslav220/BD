from http import HTTPStatus
from flask import Blueprint, Response, make_response

err_handler_bp = Blueprint('errors', __name__)

@err_handler_bp.app_errorhandler(HTTPStatus.NOT_FOUND)
def handle_404(error: Exception) -> Response:
    """Обробка помилки 404 - об'єкт не знайдено."""
    return make_response({"error": "Об'єкт не знайдено"}, HTTPStatus.NOT_FOUND)

@err_handler_bp.app_errorhandler(HTTPStatus.UNPROCESSABLE_ENTITY)
def handle_422(error: Exception) -> Response:
    """Обробка помилки 422 - вхідні дані неправильні або неповні."""
    return make_response({"error": "Вхідні дані неправильні або неповні"}, HTTPStatus.UNPROCESSABLE_ENTITY)

@err_handler_bp.app_errorhandler(HTTPStatus.CONFLICT)
def handle_409(error: Exception) -> Response:
    """Обробка помилки 409 - конфлікт даних."""
    return make_response({"error": "Такий об'єкт вже існує в базі даних"}, HTTPStatus.CONFLICT)
