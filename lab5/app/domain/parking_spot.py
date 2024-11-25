from __future__ import annotations
from typing import Dict, Any
from app import db

class ParkingSpot(db.Model):
    __tablename__ = 'parking_spot'

    spot_number = db.Column(db.Integer, primary_key=True, autoincrement=False)  # Використовуємо spot_number як первинний ключ
    parking_id = db.Column(db.Integer, db.ForeignKey('parking.id'), nullable=False)  # Зовнішній ключ

    def __repr__(self) -> str:
        return f"ParkingSpot(spot_number={self.spot_number}, parking_id={self.parking_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'spot_number': self.spot_number,
            'parking_id': self.parking_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> ParkingSpot:
        return ParkingSpot(
            spot_number=dto_dict.get('spot_number'),
            parking_id=dto_dict.get('parking_id'),
        )
