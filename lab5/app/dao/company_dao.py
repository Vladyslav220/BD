# app/dao/company_dao.py
from .general_dao import GeneralDAO
from ..domain.company import Company

class CompanyDAO(GeneralDAO):
    _domain_type = Company
