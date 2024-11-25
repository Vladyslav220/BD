from .general_controller import GeneralController
from ..service import occupancy_service


class OccupancyController(GeneralController):
    _service = occupancy_service
