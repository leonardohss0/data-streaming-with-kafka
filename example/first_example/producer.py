from kafka import KafkaProducer
import time

KAFKA_BROKER = "localhost:19092"
KAFKA_TOPIC = "first-example-topic"

producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER)

try:
    while True:
        message = input("Message: ")
        producer.send(KAFKA_TOPIC, value=message.encode("utf-8"))

except KeyboardInterrupt:
    pass
finally:
    producer.close()
