from __future__ import annotations
from typing import Dict, Any
from app import db


class CustomerCard(db.Model):
    __tablename__ = 'customer_card'

    card_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    valid_from = db.Column(db.Date, nullable=False)
    valid_until = db.Column(db.Date, nullable=False)

    def __repr__(self) -> str:
        return (f"CustomerCard(card_id={self.card_id}, customer_id={self.customer_id}, "
                f"company_id={self.company_id}, valid_from='{self.valid_from}', "
                f"valid_until='{self.valid_until}')")

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'card_id': self.card_id,
            'customer_id': self.customer_id,
            'company_id': self.company_id,
            'valid_from': self.valid_from,
            'valid_until': self.valid_until,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> CustomerCard:
        return CustomerCard(
            customer_id=dto_dict.get('customer_id'),
            company_id=dto_dict.get('company_id'),
            valid_from=dto_dict.get('valid_from'),
            valid_until=dto_dict.get('valid_until'),
        )
