from .general_service import GeneralService
from ..dao import service_dao


class SerService(GeneralService):
    _dao = service_dao
