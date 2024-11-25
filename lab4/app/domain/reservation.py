from __future__ import annotations
from typing import Dict, Any
from app import db
from datetime import datetime

class Reservation(db.Model):
    __tablename__ = 'reservation'

    parking_spot_id = db.Column(db.Integer, db.ForeignKey('parking_spot.spot_number'), primary_key=True)  # Використовуємо parking_spot_id як первинний ключ
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    reservation_time = db.Column(db.DateTime, nullable=False)

    def __repr__(self) -> str:
        return (f"Reservation(parking_spot_id={self.parking_spot_id}, "
                f"customer_id={self.customer_id}, reservation_time='{self.reservation_time}')")

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'parking_spot_id': self.parking_spot_id,
            'customer_id': self.customer_id,
            'reservation_time': self.reservation_time.isoformat(),
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Reservation:
        return Reservation(
            parking_spot_id=dto_dict.get('parking_spot_id'),
            customer_id=dto_dict.get('customer_id'),
            reservation_time=dto_dict.get('reservation_time'),
        )
