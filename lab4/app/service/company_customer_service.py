from .general_service import GeneralService
from ..dao import company_customer_dao


class CompanyCustomerService(GeneralService):
    _dao = company_customer_dao
