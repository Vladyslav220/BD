from .general_controller import GeneralController
from ..service import parking_spot_service


class ParkingSpotController(GeneralController):
    _service = parking_spot_service
