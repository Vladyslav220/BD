from .parking_service import ParkingService
from .parking_spot_service import ParkingSpotService
from .customer_service import CustomerService
from .vehicle_service import VehicleService
from .company_service import CompanyService
from .customer_card_service import CustomerCardService
from .occupancy_service import OccupancyService
from .ticket_service import TicketService
from .payment_service import PaymentService
from .reservation_service import ReservationService
from .company_customer_service import CompanyCustomerService
from .service_service import SerService

parking_service = ParkingService()
parking_spot_service = ParkingSpotService()
customer_service = CustomerService()
vehicle_service = VehicleService()
company_service = CompanyService()
customer_card_service = CustomerCardService()
occupancy_service = OccupancyService()
ticket_service = TicketService()
payment_service = PaymentService()
reservation_service = ReservationService()
company_customer_service = CompanyCustomerService()
ser_service = SerService()
