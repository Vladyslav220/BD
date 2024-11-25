from .general_controller import GeneralController
from ..service import customer_card_service


class CustomerCardController(GeneralController):
    _service = customer_card_service
