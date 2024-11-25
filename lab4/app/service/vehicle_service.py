from .general_service import GeneralService
from ..dao import vehicle_dao


class VehicleService(GeneralService):
    _dao = vehicle_dao
