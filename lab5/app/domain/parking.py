from __future__ import annotations
from typing import Dict, Any
from app import db

class Parking(db.Model):
    __tablename__ = 'parking'

    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(100), nullable=False)
    network = db.Column(db.String(50), nullable=False)
    total_spots = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return (f"Parking(id={self.id}, address='{self.address}', "
                f"network='{self.network}', total_spots={self.total_spots})")

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'address': self.address,
            'network': self.network,
            'total_spots': self.total_spots,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Parking:
        parking = Parking(
            address=dto_dict.get('address'),
            network=dto_dict.get('network'),
            total_spots=dto_dict.get('total_spots'),
        )
        return parking
