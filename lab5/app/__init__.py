import os
import pymysql
from urllib.parse import urlparse
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from app.root import register_routes

db = SQLAlchemy()

def _db_url_from_env() -> str:
    env_url = os.getenv("DATABASE_URL")
    if env_url:
        return env_url
    return "mysql+pymysql://root:root@127.0.0.1:3306/parkingdb"

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['SQLALCHEMY_DATABASE_URI'] = _db_url_from_env()
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    register_routes(app)

    if os.getenv("INIT_SQL") == "1":
        _apply_sql_dump(app)

    return app

def _apply_sql_dump(app: Flask):
    """
    Застосувати lab5/data.sql до поточної БД.
    Вмикається лише якщо INIT_SQL=1 в оточенні.
    """
    dsn = app.config['SQLALCHEMY_DATABASE_URI']
    if not dsn.startswith("mysql+pymysql://"):
        print("INIT_SQL пропущено: не MySQL+pymysql DSN")
        return

    d = urlparse(dsn.replace("mysql+pymysql://", "mysql://"))
    user = d.username
    password = d.password
    host = d.hostname
    port = d.port or 3306
    dbname = d.path.lstrip("/")

    sql_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data.sql")
    if not os.path.exists(sql_file_path):
        print(f"INIT_SQL: файл не знайдено: {sql_file_path}")
        return

    conn = pymysql.connect(host=host, user=user, password=password, database=dbname, port=port, charset="utf8mb4")
    try:
        with conn.cursor() as cur, open(sql_file_path, "r", encoding="utf-8") as f:
            sql_text = f.read()
            for stmt in [s.strip() for s in sql_text.split(";")]:
                if stmt:
                    try:
                        cur.execute(stmt)
                        conn.commit()
                    except pymysql.MySQLError as e:
                        print(f"[INIT_SQL] помилка: {e}")
                        conn.rollback()
        print("INIT_SQL: data.sql застосовано")
    finally:
        conn.close()
