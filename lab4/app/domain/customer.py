from __future__ import annotations
from typing import Dict, Any
from app import db
from .vehicle import Vehicle


class Customer(db.Model):
    __tablename__ = 'customer'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(100), nullable=False)

    # companies = db.relationship('Company', secondary='company_customer', back_populates='customer')

    # Встановлюємо релейшен до таблиці Vehicle
    # vehicles = db.relationship("Vehicle", back_populates="owner")

    def __repr__(self) -> str:
        return (f"Customer(id={self.id}, first_name='{self.first_name}', "
                f"last_name='{self.last_name}', phone_number='{self.phone_number}', "
                f"email='{self.email}')")

    def put_into_dto(self) -> Dict[str, Any]:
        # vehicles = [vehicle.put_into_dto() for vehicle in self.vehicles]
        # companies = [company.put_into_dto() for company in self.companies]
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'phone_number': self.phone_number,
            'email': self.email,
            # 'vehicles': vehicles if vehicles else None,
            # 'companies': companies
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Customer:
        customer = Customer(
            first_name=dto_dict.get('first_name'),
            last_name=dto_dict.get('last_name'),
            phone_number=dto_dict.get('phone_number'),
            email=dto_dict.get('email'),
        )
        # for vehicle_data in dto_dict.get('vehicles', []):
        #     vehicle = Vehicle.create_from_dto(vehicle_data)
        #     customer.vehicles.append(vehicle)
        return customer
