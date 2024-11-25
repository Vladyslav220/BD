from .parking_spot_dao import ParkingSpotDAO
from .customer_dao import CustomerDAO
from .vehicle_dao import VehicleDAO
from .company_dao import CompanyDAO
from .customer_card_dao import CustomerCardDAO
from .occupancy_dao import OccupancyDAO
from .ticket_dao import TicketDAO
from .payment_dao import PaymentDAO
from .parking_dao import ParkingDAO
from .reservation_dao import ReservationDAO
from .company_customer_dao import CompanyCustomerDAO
parking_spot_dao = ParkingSpotDAO()
customer_dao = CustomerDAO()
vehicle_dao = VehicleDAO()
company_dao = CompanyDAO()
customer_card_dao = CustomerCardDAO()
occupancy_dao = OccupancyDAO()
ticket_dao = TicketDAO()
payment_dao = PaymentDAO()
parking_dao = ParkingDAO()
reservation_dao = ReservationDAO()
company_customer_dao = CompanyCustomerDAO()