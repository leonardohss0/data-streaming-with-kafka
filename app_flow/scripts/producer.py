import json

from confluent_kafka import Producer

from app_flow.resources.configs import producer_settings_json, on_delivery_json


class Kafka(object):
    @staticmethod
    def json_producer(broker, object_name, kafka_topic):
        p = Producer(producer_settings_json(broker))

        get_data = object_name
        key = "wikipedia"  # Set your desired key

        try:
            p.poll(0)
            p.produce(
                topic=kafka_topic,
                key=key.encode("utf-8"),  # Encode the key as bytes
                value=json.dumps(get_data).encode("utf-8"),
                callback=on_delivery_json,
            )

        except BufferError:
            print("Buffer full")
            p.poll(0.1)

        except ValueError:
            print("Invalid input")
            raise

        except KeyboardInterrupt:
            raise

        p.flush()
