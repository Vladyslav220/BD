from .general_controller import GeneralController
from ..service import company_service


class CompanyController(GeneralController):
    _service = company_service
