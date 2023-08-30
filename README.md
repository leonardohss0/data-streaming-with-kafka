# Kafka Data Streaming Project

The Kafka Data Streaming Project is a demonstration of using Apache Kafka for real-time data streaming, processing, and storing. It primarily focuses on fetching data from the Wikipedia Data Stream, processing it, and storing the results in an AWS S3 bucket for further analysis using AWS Athena.

Keywords: Python, Data Processing, Kafka, Data Streaming, Docker

## Configuration
### Setting up the Kafka Cluster with Conduktor and Docker

Open Docker and then run the following command line in the prompt

`curl -L https://releases.conduktor.io/quick-start -o docker-compose.yml`

`docker compose up -d --wait`

`echo "Conduktor started on http://localhost:8080"`

Access the Conduktor UI on *http://localhost:8080* and then create your first topic.

## Usage
1. Clone this repository to your local machine.
2. Install the required dependencies using pip install -r requirements.txt.
3. Configure your Kafka broker, topic, and AWS credentials in the resources/configs.py file.
4. Run the Kafka producer and consumers as needed.

## Key Components:
**Kafka Producer (scripts/producer.py)**: This component fetches data from the Wikipedia Data Stream and publishes it to Kafka topics.
  
**Kafka Consumer (scripts/consumer.py)**: This component process the data published in the kafka topic.
  
**Configuration (resources/configs.py)**: Configuration settings for Kafka, AWS, and other components are stored here.

## Dependencies
Confluent Kafka: [Link to Confluent Kafka](https://github.com/confluentinc/confluent-kafka-python)

Getting Started with Conduktor: [Link to Conduktor](https://www.conduktor.io/get-started/)

Other dependencies are listed in the requirements.txt file.

## License:

This project is open-source and distributed under the MIT License, allowing for collaboration and adaptation according to your requirements.

In summary, this project showcases how to use Kafka for real-time data processing and streaming, making it a valuable resource for anyone interested in building similar data streaming solutions.
