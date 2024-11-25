from .general_controller import GeneralController
from ..service import company_customer_service


class CompanyCustomerController(GeneralController):
    _service = company_customer_service
