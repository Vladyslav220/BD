from .general_dao import GeneralDAO
from ..domain import Occupancy

class OccupancyDAO(GeneralDAO):
    _domain_type = Occupancy
