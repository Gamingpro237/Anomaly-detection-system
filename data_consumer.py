# data_consumer.py

import json
from kafka import KafkaConsumer
from utils import get_timestamp

class DataConsumer:
    def __init__(self, bootstrap_servers, topic):
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=bootstrap_servers,
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='real_time_group',
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )

    def consume_data(self):
        for message in self.consumer:
            data = message.value
            print(f"Consumed data: {data}")
            yield data

if __name__ == "__main__":
    from config import KAFKA_BOOTSTRAP_SERVERS, KAFKA_TOPIC
    consumer = DataConsumer(KAFKA_BOOTSTRAP_SERVERS, KAFKA_TOPIC)
    for data in consumer.consume_data():
        pass  # Implement processing logic here
