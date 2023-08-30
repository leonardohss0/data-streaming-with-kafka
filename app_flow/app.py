from app_flow.scripts.producer import Kafka
from app_flow.resources.configs import KAFKA_BROKER, KAFKA_TOPIC, WIKIPEDIA_STREAM_URL

import requests
import json


def fetch_latest_wikipedia_data(last_timestamp):
    response = requests.get(WIKIPEDIA_STREAM_URL, stream=True)
    for line in response.iter_lines(decode_unicode=True):
        if line.startswith("data: "):
            json_data = line[len("data: ") :]
            change = json.loads(json_data)
            change_timestamp = change.get("timestamp")
            if change_timestamp:
                change_timestamp = int(change_timestamp)
                if change_timestamp > last_timestamp:
                    yield json_data
                    last_timestamp = change_timestamp


def run():
    last_timestamp = 0

    while True:
        for data in fetch_latest_wikipedia_data(last_timestamp):
            Kafka().json_producer(
                broker=KAFKA_BROKER, object_name=data, kafka_topic=KAFKA_TOPIC
            )

            change = json.loads(data)
            last_timestamp = int(change.get("timestamp", last_timestamp))


run()
