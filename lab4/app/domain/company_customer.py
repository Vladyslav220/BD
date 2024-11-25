from __future__ import annotations
from typing import Dict, Any
from app import db


class CompanyCustomer(db.Model):
    __tablename__ = 'company_customer'

    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), primary_key=True)

    def __repr__(self) -> str:
        return (f"CompanyCustomer(company_id={self.company_id}, "
                f"customer_id={self.customer_id})")

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'company_id': self.company_id,
            'customer_id': self.customer_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> CompanyCustomer:
        return CompanyCustomer(
            company_id=dto_dict.get('company_id'),
            customer_id=dto_dict.get('customer_id'),
        )
