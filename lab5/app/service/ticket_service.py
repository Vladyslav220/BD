from .general_service import GeneralService
from ..dao import ticket_dao


class TicketService(GeneralService):
    _dao = ticket_dao
