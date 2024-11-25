from .general_dao import GeneralDAO
from ..domain import Ticket

class TicketDAO(GeneralDAO):
    _domain_type = Ticket
