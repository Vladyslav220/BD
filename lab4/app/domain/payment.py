from __future__ import annotations
from typing import Dict, Any
from app import db
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
        # Перевіряємо, чи існує квиток
        # if Ticket.query.get(dto_dict['ticket_id']) is None:
        #     raise ValueError("Ticket does not exist.")

        payment = Payment(
            ticket_id=dto_dict.get('ticket_id'),
            amount=dto_dict.get('amount'),
            payment_time=dto_dict.get('payment_time'),
        )
        db.session.add(payment)
        db.session.commit()
        return payment
