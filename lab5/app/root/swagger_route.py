from flask import Blueprint, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint
import os

swagger_bp = Blueprint("swagger_json", __name__)

@swagger_bp.route("/swagger.json")
def swagger_json():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    return send_from_directory(base_dir, "swagger.json")

SWAGGER_URL = "/swagger"
API_URL = "/swagger.json"

swagger_ui_bp = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={"app_name": "Parking API (lab5)"}
)
