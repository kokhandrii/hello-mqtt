from functools import partial
from time import sleep

import paho.mqtt.client as mqtt
# connect_callback(client, userdata, flags, reasonCode, properties)
import upsidedown as upsidedown


def on_connect_subscribe(topic, client: mqtt.Client, userdata, flags, reasonCode, properties=None):
    print(f'on connect, subscribing to topic {topic}')
    client.subscribe(topic)


class MyMessageProcessor:
    @staticmethod
    def transform(message: mqtt.MQTTMessage) -> str:
        return upsidedown.transform(str(message.payload).upper())


def on_message_callback(client, userdata, message: mqtt.MQTTMessage):
    original_message = message.payload
    print('original message: ', original_message)

    # done via message processor + upper case
    processor = MyMessageProcessor()
    result = processor.transform(message)
    print('message Processor upper case', result)

    # done via lambda + reverse string
    result = lambda _: processor.transform(message)
    print('lambda reverse string: ', result(str(original_message)[::-1]))

    # done via itertools.partial + upside down
    result = partial(upsidedown.transform, str(message))
    print('partial upside down: ', result(transliterations={'ö': 'oe'}))


def main(host: str, port: str, topic: str):
    client = mqtt.Client()
    while True:
        try:
            print(f'connecting to {host}:{port}')
            client.connect(host, port, 20)
        except Exception as e:
            print(e)
            print("backoff...")
            sleep(10)
        else:
            print('connected')
            break
    client.on_connect = partial(on_connect_subscribe, topic)
    client.on_message = on_message_callback
    client.loop_forever(retry_first_connection=True)
