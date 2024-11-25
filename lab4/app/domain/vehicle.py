from __future__ import annotations
from typing import Dict, Any
from app import db


class Vehicle(db.Model):
    __tablename__ = 'vehicle'

    vehicle_id = db.Column(db.Integer, primary_key=True)
    plate_number = db.Column(db.String(10), unique=True, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)

    # Встановлюємо релейшен до таблиці Customer
    # owner = db.relationship("Customer", back_populates="vehicles")

    def __repr__(self) -> str:
        return (f"Vehicle(vehicle_id={self.vehicle_id}, plate_number='{self.plate_number}', "
                f"owner_id={self.owner_id})")

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'vehicle_id': self.vehicle_id,
            'plate_number': self.plate_number,
            'owner_id': self.owner_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Vehicle:
        return Vehicle(
            plate_number=dto_dict.get('plate_number'),
            owner_id=dto_dict.get('owner_id'),
        )
