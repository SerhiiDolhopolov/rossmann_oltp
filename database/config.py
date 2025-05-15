from dotenv import load_dotenv
import os


load_dotenv()

OLTP_USER = os.getenv("OLTP_USER")
OLTP_PASSWORD = os.getenv("OLTP_PASSWORD")
OLTP_HOST = os.getenv("OLTP_HOST")
OLTP_PORT = os.getenv("OLTP_PORT")
OLTP_DB = os.getenv("OLTP_DB")

DATE_TIME_FORMAT = os.getenv("DATE_TIME_FORMAT", "%Y-%m-%d %H:%M:%S")
KAFKA_HOST = os.getenv("KAFKA_HOST")
KAFKA_PORT = os.getenv("KAFKA_PORT")
KAFKA_TOPIC_OLTP_UPDATE_PRODUCT_QUANTITY = os.getenv("KAFKA_TOPIC_OLTP_UPDATE_PRODUCT_QUANTITY")