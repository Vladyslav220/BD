from __future__ import annotations
from typing import Dict, Any
from app import db
from .vehicle import Vehicle

class Occupancy(db.Model):
    __tablename__ = 'occupancy'

    occupancy_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    spot_number = db.Column(db.Integer, db.ForeignKey('parking_spot.spot_number'), nullable=False)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.vehicle_id'), nullable=False)
    entry_time = db.Column(db.DateTime, nullable=False)
    exit_time = db.Column(db.DateTime, nullable=False)

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'occupancy_id': self.occupancy_id,
            'spot_number': self.spot_number,
            'vehicle_id': self.vehicle_id,
            'entry_time': self.entry_time,
            'exit_time': self.exit_time,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Occupancy:
        # Перевіряємо, чи існує транспортний засіб
        # if Vehicle.query.get(dto_dict['vehicle_id']) is None:
        #     raise ValueError("Vehicle does not exist.")

        occupancy = Occupancy(
            spot_number=dto_dict.get('spot_number'),
            vehicle_id=dto_dict.get('vehicle_id'),
            entry_time=dto_dict.get('entry_time'),
            exit_time=dto_dict.get('exit_time'),
        )
        db.session.add(occupancy)
        db.session.commit()
        return occupancy
