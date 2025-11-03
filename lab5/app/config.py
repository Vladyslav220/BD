import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "mysql+pymysql://admin:NewStrongPass!123@database-lab-1.c3u0c6k0idq9.eu-north-1.rds.amazonaws.com:3306/parkingdb"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "change-me")
