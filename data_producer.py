import json
import time
import random
from kafka import KafkaProducer
from utils import get_timestamp

class DataProducer:
    def __init__(self, bootstrap_servers, topic):
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        self.topic = topic

    def produce_data(self):
        while True:
            data = {
                "timestamp": get_timestamp(),
                "sensor_id": random.randint(1, 100),
                "value": random.uniform(10.0, 100.0),
                "document": f"Document content {random.randint(1, 1000)}"
            }
            self.producer.send(self.topic, data)
            print(f"Produced data: {data}")
            time.sleep(1)  # Produce data every second

if __name__ == "__main__":
    from config import KAFKA_BOOTSTRAP_SERVERS, KAFKA_TOPIC
    producer = DataProducer(KAFKA_BOOTSTRAP_SERVERS, KAFKA_TOPIC)
    producer.produce_data()
