from .general_dao import GeneralDAO
from ..domain import ParkingSpot

class ParkingSpotDAO(GeneralDAO):
    _domain_type = ParkingSpot