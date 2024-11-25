from .general_dao import GeneralDAO
from ..domain import Vehicle

class VehicleDAO(GeneralDAO):
    _domain_type = Vehicle
