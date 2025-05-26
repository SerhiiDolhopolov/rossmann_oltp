import json
import time
import logging

from confluent_kafka import Consumer, KafkaException, KafkaError
from database.config import (
    KAFKA_TOPIC_OLTP_UPDATE_PRODUCT_QUANTITY,
    KAFKA_HOST,
    KAFKA_PORT,
)
from database.services.sync_service import update_products_quantity
from database.db import get_db
from config import init_logging

init_logging()
logger = logging.getLogger(__name__)


def consume_messages(topic_handlers: dict[str, callable]):
    def connect_consumer():
        consumer = Consumer(
            {
                "bootstrap.servers": f"{KAFKA_HOST}:{KAFKA_PORT}",
                "group.id": "rossmann-oltp-group",
                "auto.offset.reset": "latest",
                "logger": logging.getLogger("confluent_kafka"),
            }
        )
        topics = list(topic_handlers.keys())
        consumer.subscribe(topics)
        logger.info("Consumer started. Subscribed to topics: %s", topics)

        while not consumer.assignment():
            logger.info("Waiting for partition assignment...")
            consumer.poll(1.0)
            time.sleep(5)
        logger.info("Assigned partitions: %s", consumer.assignment())
        return consumer

    def reconnect_consumer(consumer) -> Consumer:
        if consumer:
            consumer.close()
        time.sleep(5)
        return connect_consumer()

    consumer = connect_consumer()
    try:
        while True:
            try:
                msg = consumer.poll(1.0)
                if msg is None:
                    continue
                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        logger.debug(
                            "End of partition reached: %s [%s]",
                            msg.topic(),
                            msg.partition(),
                        )
                    else:
                        logger.error("Kafka error: %s", msg.error())
                        consumer = reconnect_consumer(consumer)
                        continue
                topic = msg.topic()
                value = msg.value().decode("utf-8")
                logger.debug("Topic: %s\nReceived message: %s", topic, value)
                if topic in topic_handlers:
                    try:
                        topic_handlers[topic](value)
                    except Exception:
                        logger.error(
                            "Error processing message: %s", exc_info=True)
            except KafkaException as e:
                logger.error("Kafka exception: %s. Reconnect...", e)
                consumer = reconnect_consumer(consumer)
    finally:
        consumer.close()


def update_product_quantity_by_kafka(value: str):
    data = json.loads(value)
    db = next(get_db())
    try:
        shop_id = int(data["shop_id"])
        updated_products = {int(k): int(v)
                            for k, v in data["updated_products"].items()}
        update_products_quantity(db, shop_id, updated_products)
    finally:
        db.close()


if __name__ == "__main__":
    consume_messages(
        {KAFKA_TOPIC_OLTP_UPDATE_PRODUCT_QUANTITY: update_product_quantity_by_kafka}
    )
