import pymysql
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from app.root import register_routes
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1/parkingdb'
    db.init_app(app)
    register_routes(app)
    create_database()
    create_tables(app)
    populate_data()
    return app

def create_database():
    connection = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='root'
    )
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS parkingdb")
    cursor.close()
    connection.close()

def create_tables(app):
    with app.app_context():
        db.create_all()

def populate_data():
    sql_file_path = os.path.abspath('data.sql')
    if os.path.exists(sql_file_path):
        connection = pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='root',
            database='parkingdb'
        )
        cursor = connection.cursor()
        with open(sql_file_path, 'r', encoding='utf-8') as sql_file:  # Додано кодування
            sql_text = sql_file.read()
            sql_statements = sql_text.split(';')
            for statement in sql_statements:
                statement = statement.strip()
                if statement:
                    try:
                        cursor.execute(statement)
                        connection.commit()
                    except pymysql.MySQLError as error:
                        print(f"Error executing SQL statement: {error}")
                        connection.rollback()
        cursor.close()
        connection.close()
