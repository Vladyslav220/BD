from .general_dao import GeneralDAO
from ..domain import CustomerCard

class CustomerCardDAO(GeneralDAO):
    _domain_type = CustomerCard
