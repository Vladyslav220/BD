from __future__ import annotations
from typing import Dict, Any
from app import db
from sqlalchemy import event, select


class Service(db.Model):
    __tablename__ = 'service'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=True)
    cost = db.Column(db.Float, nullable=False)
    customer_id = db.Column(db.Integer, nullable=False)  # Removed ForeignKey constraint

    def __repr__(self) -> str:
        return (f"Service(id={self.id}, name={self.name}, description={self.description}, "
                f"cost={self.cost}, customer_id={self.customer_id})")

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'cost': self.cost,
            'customer_id': self.customer_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Service:
        return Service(
            name=dto_dict.get('name'),
            description=dto_dict.get('description'),
            cost=dto_dict.get('cost'),
            customer_id=dto_dict.get('customer_id'),
        )


# Event listener to check if customer exists before insert
@event.listens_for(Service, "before_insert")
def check_customer_exists(mapper, connection, target):
    customer_table = db.Table('customer', db.metadata, autoload_with=db.engine)

    customer_exists = connection.execute(
        select(customer_table.c.id).where(customer_table.c.id == target.customer_id)
    ).first()

    if not customer_exists:
        raise ValueError(f"Customer with id {target.customer_id} does not exist in customer table.")
