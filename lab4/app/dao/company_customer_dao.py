from .general_dao import GeneralDAO
from ..domain import CompanyCustomer

class CompanyCustomerDAO(GeneralDAO):
    _domain_type = CompanyCustomer
