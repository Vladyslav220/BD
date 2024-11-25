from .general_service import GeneralService
from ..dao import occupancy_dao


class OccupancyService(GeneralService):
    _dao = occupancy_dao
