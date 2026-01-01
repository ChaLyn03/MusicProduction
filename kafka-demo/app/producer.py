from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

for i in range(20):
    message = {
        "sensor": "alpha",
        "reading": random.randint(0, 120),
        "seq": i,
    }
    producer.send("test-topic", message)
    print("sent:", message)
    time.sleep(0.5)

producer.flush()
