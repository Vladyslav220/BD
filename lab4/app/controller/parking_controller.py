from .general_controller import GeneralController
from ..service import parking_service


class ParkingController(GeneralController):
    _service = parking_service
