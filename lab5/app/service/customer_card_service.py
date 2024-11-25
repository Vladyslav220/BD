from .general_service import GeneralService
from ..dao import customer_card_dao


class CustomerCardService(GeneralService):
    _dao = customer_card_dao
