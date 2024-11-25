from .general_service import GeneralService
from ..dao import payment_dao


class PaymentService(GeneralService):
    _dao = payment_dao
