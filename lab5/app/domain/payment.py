from __future__ import annotations
from typing import Dict, Any, Optional
from app import db
from sqlalchemy import func
from .ticket import Ticket


class Payment(db.Model):
    __tablename__ = 'payment'

    ticket_id = db.Column(db.Integer, db.ForeignKey('ticket.id'), primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    payment_time = db.Column(db.DateTime, nullable=False)

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'ticket_id': self.ticket_id,
            'amount': self.amount,
            'payment_time': self.payment_time,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Payment:
        payment = Payment(
            ticket_id=dto_dict.get('ticket_id'),
            amount=dto_dict.get('amount'),
            payment_time=dto_dict.get('payment_time'),
        )
        db.session.add(payment)
        db.session.commit()
        return payment

    @staticmethod
    def calculate_column(operation: str, column_name: str) -> Optional[float]:
        operations = {
            'max': func.max,
            'min': func.min,
            'sum': func.sum,
            'avg': func.avg
        }

        if operation not in operations:
            raise ValueError(f"Unsupported operation: {operation}")

        column = getattr(Payment, column_name)
        query = db.session.query(operations[operation](column)).scalar()

        return query
