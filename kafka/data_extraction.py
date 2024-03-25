import requests
import polars as pl
from confluent_kafka import Producer


def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data from {url}")
        return None


def create_dataframe(data):
    if data:
        df = pl.DataFrame(data)
        return df
    else:
        return None


def produce_message(producer, topic, message):
    producer.produce(topic, message.encode("utf-8"))
    producer.flush()


def main():
    # Central Bank of Brazil API URLs
    inflation_url = (
        "https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/ultimos/30?formato=json"
    )
    job_rates_url = (
        "https://api.bcb.gov.br/dados/serie/bcdata.sgs.24369/ultimos/30?formato=json"
    )
    interest_rates_url = (
        "https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/ultimos/30?formato=json"
    )
    public_spending_url = (
        "https://api.bcb.gov.br/dados/serie/bcdata.sgs.4426/ultimos/30?formato=json"
    )

    # Fetching data
    inflation_data = fetch_data(inflation_url)
    job_rates_data = fetch_data(job_rates_url)
    interest_rates_data = fetch_data(interest_rates_url)
    public_spending_data = fetch_data(public_spending_url)

    # Creating DataFrames
    inflation_df = create_dataframe(inflation_data)
    job_rates_df = create_dataframe(job_rates_data)
    interest_rates_df = create_dataframe(interest_rates_data)
    public_spending_df = create_dataframe(public_spending_data)

    # Kafka Producer
    kafka_bootstrap_servers = "localhost:9092"
    kafka_topic = "brazil_data"

    producer_conf = {"bootstrap.servers": kafka_bootstrap_servers}
    producer = Producer(producer_conf)

    # Sending data to Kafka topic
    if inflation_df is not None:
        produce_message(producer, kafka_topic, inflation_df.to_json())
    if job_rates_df is not None:
        produce_message(producer, kafka_topic, job_rates_df.to_json())
    if interest_rates_df is not None:
        produce_message(producer, kafka_topic, interest_rates_df.to_json())
    if public_spending_df is not None:
        produce_message(producer, kafka_topic, public_spending_df.to_json())


if __name__ == "__main__":
    main()
