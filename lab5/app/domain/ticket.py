from __future__ import annotations
from typing import Dict, Any
from app import db
from sqlalchemy import event, select
from datetime import datetime

class Ticket(db.Model):
    __tablename__ = 'ticket'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    spot_number = db.Column(db.Integer, db.ForeignKey('parking_spot.spot_number'), nullable=False)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.vehicle_id'), nullable=False)
    issue_time = db.Column(db.DateTime, nullable=False)

    # vehicle = db.relationship("Vehicle")

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'spot_number': self.spot_number,
            'vehicle_id': self.vehicle_id,
            'issue_time': self.issue_time,
        }


    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Ticket:
        # Перевіряємо, чи існує транспортний засіб
        # if Vehicle.query.get(dto_dict['vehicle_id']) is None:
        #     raise ValueError("Vehicle does not exist.")

        ticket = Ticket(
            spot_number=dto_dict.get('spot_number'),
            vehicle_id=dto_dict.get('vehicle_id'),
            issue_time=dto_dict.get('issue_time'),
        )
        db.session.add(ticket)
        db.session.commit()
        return ticket
