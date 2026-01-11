import boto3
import pandas as pd
import os
from io import StringIO

BUCKET = os.environ["S3_BUCKET"]
ENDPOINT = os.environ["AWS_ENDPOINT_URL"]

s3 = boto3.client(
    "s3",
    endpoint_url=ENDPOINT,
    aws_access_key_id="test",
    aws_secret_access_key="test",
    region_name="us-east-1",
)

# Read CSV from raw
obj = s3.get_object(Bucket=BUCKET, Key="raw/sample_data.csv")
df = pd.read_csv(obj["Body"])

# Transform: keep people older than 30
df = df[df["age"] > 30]
df["tax"] = df["salary"] * 0.10

# Save result
buffer = StringIO()
df.to_csv(buffer, index=False)

s3.put_object(
    Bucket=BUCKET,
    Key="processed/output.csv",
    Body=buffer.getvalue()
)

print("ETL SUCCESS")
