from .general_dao import GeneralDAO
from ..domain import Service


class ServiceDAO(GeneralDAO):
    _domain_type = Service
