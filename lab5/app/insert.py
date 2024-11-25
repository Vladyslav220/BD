from flask import jsonify, make_response, request
from http import HTTPStatus
from app import db

def insert_record(model, data):
    """
    Універсальна функція для вставки запису в таблицю.
    """
    try:
        record = model(**data)
        db.session.add(record)
        db.session.commit()
        return make_response(jsonify(record.put_into_dto()), HTTPStatus.CREATED)
    except Exception as e:
        db.session.rollback()
        return make_response({'error': str(e)}, HTTPStatus.BAD_REQUEST)
