from confluent_kafka import Consumer, KafkaError
import os

import pandas as pd
from io import StringIO
import boto3
import time
import json
from datetime import datetime

AWS_ACCESS_ID = os.environ.get("AWS_ACCESS_ID")
AWS_ACCESS_KEY = os.environ.get("AWS_ACCESS_KEY")

KAFKA_BROKER = "localhost:19092"
KAFKA_TOPIC = "my-topic"


def pushToLake(df_data, name):
    bucket = "kafka-bench-de"  # already created on S3
    csv_buffer = StringIO()
    df_data.to_csv(csv_buffer, encoding="utf8", index=False)
    schema = "wiki/"
    s3_resource = boto3.resource(
        "s3", aws_access_key_id=AWS_ACCESS_ID, aws_secret_access_key=AWS_ACCESS_KEY
    )
    file_name = name + ".csv"
    s3_resource.Object(
        bucket, schema + str(time.strftime("%Y/%m/%d/")) + file_name
    ).put(Body=csv_buffer.getvalue())


def consumer_settings_json(broker):
    json = {
        "bootstrap.servers": broker,
        "group.id": "consumer-group",
        "auto.commit.interval.ms": 6000,
        "auto.offset.reset": "earliest",
    }

    return dict(json)


def run():
    execution_time = 100

    c = Consumer(consumer_settings_json(KAFKA_BROKER))
    c.subscribe([KAFKA_TOPIC])

    timeout = time.time() + int(execution_time)

    try:
        while timeout >= time.time():
            msg = c.poll(0.1)

            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(msg.error())
                    break

            print("Received message: {}".format(msg.value().decode("utf-8")))

            json_data = json.loads(msg.value().decode("utf-8"))

            df = pd.DataFrame([json_data])
            df[0] = df[0].apply(json.loads)
            new_df = pd.DataFrame(df[0].tolist())

            current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S.%f")
            # pushToLake(new_df, "wiki_" + current_datetime)

    except KeyboardInterrupt:
        pass

    finally:
        c.close()


run()
