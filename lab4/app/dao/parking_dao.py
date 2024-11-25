from .general_dao import GeneralDAO
from ..domain import Parking

class ParkingDAO(GeneralDAO):
    _domain_type = Parking
