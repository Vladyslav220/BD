from .general_dao import GeneralDAO
from ..domain import Payment

class PaymentDAO(GeneralDAO):
    _domain_type = Payment
