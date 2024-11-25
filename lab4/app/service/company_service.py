from .general_service import GeneralService
from ..dao import company_dao


class CompanyService(GeneralService):
    _dao = company_dao
