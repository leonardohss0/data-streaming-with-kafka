from kafka import KafkaProducer
import time

KAFKA_BROKER = "localhost:19092"
KAFKA_TOPIC = "demo-topic"

producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER)

try:
    message_counter = 1
    while True:
        message = f"Message {message_counter}"
        producer.send(KAFKA_TOPIC, value=message.encode("utf-8"))
        print(f"Sent: {message}")
        message_counter += 1
        time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    producer.close()
