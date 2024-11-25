from .general_controller import GeneralController
from ..service import vehicle_service


class VehicleController(GeneralController):
    _service = vehicle_service
