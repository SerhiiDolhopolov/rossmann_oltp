import json
from confluent_kafka import Consumer, KafkaException, KafkaError
from database.config import KAFKA_TOPIC_OLTP_UPDATE_PRODUCT_QUANTITY, KAFKA_HOST, KAFKA_PORT
from database.services.sync_service import update_products_quantity
from database.db import get_db
import time


def consume_messages(topic_handlers: dict[str, callable]):
    def create_consumer():
        return Consumer({
            'bootstrap.servers': f'{KAFKA_HOST}:{KAFKA_PORT}',
            'group.id': 'rossmann-oltp-group',
            'auto.offset.reset': 'latest'
        })

    consumer = create_consumer()
    topics = list(topic_handlers.keys())
    consumer.subscribe(topics)
    print(f"Consumer started. Subscribed to topics: {topics}")

    while not consumer.assignment():
        print("Waiting for partition assignment...")
        consumer.poll(1.0)

    print(f"Assigned partitions: {consumer.assignment()}")

    try:
        while True:
            try:
                msg = consumer.poll(1.0)
            except KafkaException as e:
                print(f"KafkaException: {e}. Reconnect at 5 seconds...")
                consumer.close()
                time.sleep(5)
                consumer = create_consumer()
                consumer.subscribe(topics)
                continue
            except Exception as e:
                print(f"Message receiving error: {e}. Reconnect at 5 seconds...")
                consumer.close()
                time.sleep(5)
                consumer = create_consumer()
                consumer.subscribe(topics)
                continue

            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    print(f"Reached end of partition: {msg.topic()} [{msg.partition()}]")
                elif msg.error():
                    print(f"Kafka error: {msg.error()}. Попытка переподключения через 5 секунд...")
                    consumer.close()
                    time.sleep(5)
                    consumer = create_consumer()
                    consumer.subscribe(topics)
                continue

            topic = msg.topic()
            value = msg.value().decode("utf-8")
            print(f"Received message from topic '{topic}': {value}")

            if topic in topic_handlers:
                try:
                    topic_handlers[topic](value)
                except Exception as e:
                    print(f"Error processing message: {e}")
    except KeyboardInterrupt:
        print("Consumer stopped by user.")
    finally:
        consumer.close()


def update_product_quantity_by_kafka(value: str):
    data = json.loads(value)
    db = next(get_db())
    try:
        shop_id = int(data['shop_id'])
        updated_products = {int(k): int(v) for k, v in data['updated_products'].items()}
        update_products_quantity(db, shop_id, updated_products)
    finally:
        db.close()


if __name__ == "__main__":
    consume_messages({
        KAFKA_TOPIC_OLTP_UPDATE_PRODUCT_QUANTITY: update_product_quantity_by_kafka
    })