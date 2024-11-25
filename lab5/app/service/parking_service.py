from .general_service import GeneralService
from ..dao import parking_dao


class ParkingService(GeneralService):
    _dao = parking_dao
