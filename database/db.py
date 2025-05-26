import os

from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker

from rossmann_oltp_models import Base, Shop
from database.config import OLTP_USER, OLTP_PASSWORD, OLTP_DB, OLTP_HOST, OLTP_PORT

DATABASE_URL = (
    "postgresql+psycopg2://{username}:{password}@{host}:{port}/{dbname}".format(
        username=OLTP_USER,
        password=OLTP_PASSWORD,
        dbname=OLTP_DB,
        host=OLTP_HOST,
        port=OLTP_PORT,
    )
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    Base.metadata.create_all(bind=engine)
    create_triggers(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_triggers(engine):
    wait_for_tables(engine, [
        "products", "categories", "city_products", "employees"
    ])

    db = next(get_db())
    try:
        if db.query(Shop).count() > 0:
            return
    finally:
        db.close()

    triggers_path = os.path.join(os.path.dirname(__file__), "triggers.sql")
    with open(triggers_path, "r", encoding="utf-8") as file:
        sql = file.read()
    with engine.connect() as connection:
        connection.exec_driver_sql(sql)
        connection.commit()


def wait_for_tables(engine, table_names):
    inspector = inspect(engine)
    while True:
        existing = inspector.get_table_names()
        if all(t in existing for t in table_names):
            break
