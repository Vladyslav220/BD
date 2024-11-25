from .general_controller import GeneralController
from ..service import payment_service


class PaymentController(GeneralController):
    _service = payment_service
