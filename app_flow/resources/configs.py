import os

KAFKA_BROKER = "localhost:19092"
KAFKA_TOPIC = "my-topic"
WIKIPEDIA_STREAM_URL = "https://stream.wikimedia.org/v2/stream/recentchange"

AWS_ACCESS_ID = os.environ.get("AWS_ACCESS_ID")
AWS_ACCESS_KEY = os.environ.get("AWS_ACCESS_KEY")


def producer_settings_json(broker):
    json = {
        "client.id": "kafka-basics",
        "bootstrap.servers": broker,
        "acks": "all",
        "enable.idempotence": "true",
        "linger.ms": 100,
        "batch.size": 100,
        "compression.type": "gzip",
        "max.in.flight.requests.per.connection": 5,
    }

    return dict(json)


def on_delivery_json(err, msg):
    if err is not None:
        print("message delivery failed: {}".format(err))
    else:
        print(
            "message successfully produced to {} [{}] at offset {}".format(
                msg.topic(), msg.partition(), msg.offset()
            )
        )


def on_delivery_avro(err, msg, obj):
    if err is not None:
        print(
            "message {} delivery failed ofr user {} with error {}".format(
                obj, obj.name, err
            )
        )
    else:
        print(
            "message {} successfully produced to {} [{}] at offset {}".format(
                obj, msg.topic(), msg.partition(), msg.offset()
            )
        )
