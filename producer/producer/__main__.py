from producer import produce, BROKER_HOST, BROKER_PORT, TOPIC

if __name__ == '__main__':
    produce.main(
        host=BROKER_HOST,
        port=BROKER_PORT,
        topic=TOPIC
    )
