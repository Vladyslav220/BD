from .general_controller import GeneralController
from ..service import ser_service


class ServiceController(GeneralController):
    _service = ser_service
