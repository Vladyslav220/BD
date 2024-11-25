from .general_controller import GeneralController
from ..service import ticket_service


class TicketController(GeneralController):
    _service = ticket_service
