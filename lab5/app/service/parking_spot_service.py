from .general_service import GeneralService
from ..dao import parking_spot_dao


class ParkingSpotService(GeneralService):
    _dao = parking_spot_dao
