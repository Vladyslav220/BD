from flask import Flask

from .error_handler import err_handler_bp

def register_routes(app: Flask) -> None:
    app.register_blueprint(err_handler_bp)
    from .parking_route import parking_bp
    from .parking_spot_route import parking_spot_bp
    from .customer_route import customer_bp
    from .vehicle_route import vehicle_bp
    from .company_route import company_bp
    from .customer_card_route import customer_card_bp
    from .occupancy_route import occupancy_bp
    from .ticket_route import ticket_bp
    from .payment_route import payment_bp
    from .reservation_route import reservation_bp
    from .company_customer_route import company_customer_bp
    from .service_route import service_bp

    app.register_blueprint(parking_bp)
    app.register_blueprint(parking_spot_bp)
    app.register_blueprint(customer_bp)
    app.register_blueprint(vehicle_bp)
    app.register_blueprint(company_bp)
    app.register_blueprint(customer_card_bp)
    app.register_blueprint(occupancy_bp)
    app.register_blueprint(ticket_bp)
    app.register_blueprint(payment_bp)
    app.register_blueprint(reservation_bp)
    app.register_blueprint(company_customer_bp)
    app.register_blueprint(service_bp)
