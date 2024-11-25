from __future__ import annotations
from random import randint, choice
from sqlalchemy.sql import text
from datetime import time
from typing import Dict, Any
from app import db

class Company(db.Model):
    __tablename__ = 'company'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    company_name = db.Column(db.String(50), nullable=False)
    contact_person = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(100), nullable=False)

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


def create_dynamic_tables_from_companies():
    companies = Company.query.all()
    if not companies:
        return "No companies found in the database."
    table_count = randint(1, 11)
    created_tables = []

    for company in companies:
        # Формування унікальної назви таблиці
        company_name = company.company_name.replace(" ", "_")
        table_name = f"{company_name}_{str(time()).replace(':', '_')}"

        column_defs = []
        for i in range(randint(1, 9)):
            column_name = f"column_{i + 1}"
            column_type = choice(["INT", "VARCHAR(255)", "DATE"])
            column_defs.append(f"{column_name} {column_type}")
        column_defs_str = ", ".join(column_defs)

        create_table_sql = text(f"CREATE TABLE {table_name} (id INT PRIMARY KEY AUTO_INCREMENT,"
                                f" {column_defs_str});")

        db.session.execute(create_table_sql)
        db.session.commit()
        created_tables.append(table_name)

    return created_tables