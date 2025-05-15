from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from rossmann_oltp_models import Base
from database.config import OLTP_USER, OLTP_PASSWORD, OLTP_DB, OLTP_HOST, OLTP_PORT


DATABASE_URL = "postgresql+psycopg2://{username}:{password}@{host}:{port}/{dbname}".format(
    username=OLTP_USER,
    password=OLTP_PASSWORD,
    dbname=OLTP_DB,
    host=OLTP_HOST,
    port=OLTP_PORT,
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)
    
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    