from kafka import KafkaConsumer
import json

THRESHOLD = 80

def safe_deserialize(v: bytes):
    try:
        return json.loads(v.decode("utf-8"))
    except Exception:
        return {"raw": v.decode("utf-8"), "parse_error": True}

consumer = KafkaConsumer(
    "test-topic",
    bootstrap_servers="localhost:9092",
    value_deserializer=safe_deserialize,
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="monitoring-service",
)

for msg in consumer:
    data = msg.value

    # If parse failed, log and skip
    if data.get("parse_error"):
        print("WARN: bad message:", data)
        continue

    reading = data.get("reading")
    sensor = data.get("sensor")
    seq = data.get("seq")

    if reading is None:
        print("WARN: missing reading field:", data)
        continue

    if reading > THRESHOLD:
        print(f"ALERT: {sensor} reading {reading} > {THRESHOLD} (seq={seq})")
    else:
        print(f"OK: {sensor} reading {reading} (seq={seq})")
