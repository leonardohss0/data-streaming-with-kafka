from kafka import KafkaConsumer

KAFKA_BROKER = "localhost:19092"
KAFKA_TOPIC = "first-example-topic"
CONSUMER_GROUP_ID = "first-example-consumer-group"

consumer = KafkaConsumer(
    KAFKA_TOPIC,
    group_id=CONSUMER_GROUP_ID,
    bootstrap_servers=KAFKA_BROKER,
    auto_offset_reset="earliest",
)

try:
    for message in consumer:
        print(f"Received: {message.value.decode('utf-8')}")
except KeyboardInterrupt:
    pass
finally:
    consumer.close()
