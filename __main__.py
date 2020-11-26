from consumer import TOPIC, BROKER_PORT, BROKER_HOST
from consumer import consume_task

if __name__ == '__main__':
    consume_task.main(
        host=BROKER_HOST,
        port=BROKER_PORT,
        topic=TOPIC
    )
