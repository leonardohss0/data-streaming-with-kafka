from io import StringIO
import boto3
import time


def pushToLake(df_data, name, aws_access_id, aws_access_key):
    bucket = "kafka"  # already created on S3
    csv_buffer = StringIO()
    df_data.to_csv(csv_buffer, encoding="utf8", index=False)
    schema = name + "/"
    s3_resource = boto3.resource(
        "s3", aws_access_key_id=aws_access_id, aws_secret_access_key=aws_access_key
    )
    file_name = name + ".csv"
    s3_resource.Object(
        bucket, schema + str(time.strftime("%Y/%m/%d/")) + file_name
    ).put(Body=csv_buffer.getvalue())
