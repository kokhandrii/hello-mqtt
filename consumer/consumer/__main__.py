from consumer import consume, TOPIC, BROKER_PORT, BROKER_HOST

if __name__ == '__main__':
    consume.main(
        host=BROKER_HOST,
        port=BROKER_PORT,
        topic=TOPIC
    )
