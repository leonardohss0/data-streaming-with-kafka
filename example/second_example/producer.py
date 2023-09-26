from kafka import KafkaProducer
import time

KAFKA_BROKER = "localhost:19092"
KAFKA_TOPIC = "second-example-topic"

producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER)

try:
    message_counter = 1
    while True:
        message = f"Message {message_counter}"
        # key = f"Key {message_counter}"
        metadata = producer.send(
            KAFKA_TOPIC,
            # key=key.encode("utf-8"),
            value=message.encode("utf-8"),
        ).get()

        print(
            f"Sent: {message}, (Partition: {metadata.partition}, Offset: {metadata.offset})"
            # f"Sent: {message} with Key: {key} (Partition: {metadata.partition}, Offset: {metadata.offset})"
        )

        message_counter += 1
        time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    producer.close()
