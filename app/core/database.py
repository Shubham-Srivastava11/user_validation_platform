import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DB_TYPE = os.getenv("DB_TYPE", "sqlite")

if DB_TYPE == "mysql":

    DATABASE_URL = (
        f"mysql+mysqlconnector://root:password@localhost:3306/user_validation"
    )

else:

    DATABASE_URL = "sqlite:///./user_validation.db"


engine = create_engine(
    DATABASE_URL,
    echo=False,
    connect_args={"check_same_thread": False}
    if "sqlite" in DATABASE_URL else {}
)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
