from dotenv import load_dotenv
import os

load_dotenv()


DATE_TIME_FORMAT = os.getenv("DATE_TIME_FORMAT", "%Y-%m-%d %H:%M:%S")
KAFKA_HOST = os.getenv("KAFKA_HOST")
KAFKA_PORT = os.getenv("KAFKA_PORT")
KAFKA_TOPIC_OLTP_UPDATE_PRODUCT_QUANTITY = os.getenv("KAFKA_TOPIC_OLTP_UPDATE_PRODUCT_QUANTITY")