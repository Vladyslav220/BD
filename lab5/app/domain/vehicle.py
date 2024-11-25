from __future__ import annotations
from typing import Dict, Any, List
from app import db


class Vehicle(db.Model):
    __tablename__ = 'vehicle'

    vehicle_id = db.Column(db.Integer, primary_key=True)
    plate_number = db.Column(db.String(10), unique=True, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)

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


def insert_random_vehicles() -> List[Vehicle]:
    vehicles = []
    for i in range(1, 11):
        vehicle = Vehicle(
            plate_number=f"Noname{i}",
            owner_id=1,
        )
        db.session.add(vehicle)
        vehicles.append(vehicle)
    db.session.commit()
    print("10 записів успішно додано до таблиці 'vehicle'.")
    return vehicles
