from __future__ import annotations
from typing import Dict, Any
from app import db

class Company(db.Model):
    __tablename__ = 'company'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    company_name = db.Column(db.String(50), nullable=False)
    contact_person = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(100), nullable=False)

    # customer = db.relationship('Customer', secondary='company_customer', back_populates='company')
    # Приберіть реляцію з CompanyCustomer
    # customers = db.relationship("CompanyCustomer", back_populates="company", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return (f"Company(id={self.id}, company_name='{self.company_name}', "
                f"contact_person='{self.contact_person}', phone_number='{self.phone_number}', "
                f"email='{self.email}')")

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'company_id': self.id,
            'company_name': self.company_name,
            'contact_person': self.contact_person,
            'phone_number': self.phone_number,
            'email': self.email,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Company:
        return Company(
            company_name=dto_dict.get('company_name'),
            contact_person=dto_dict.get('contact_person'),
            phone_number=dto_dict.get('phone_number'),
            email=dto_dict.get('email'),
        )
