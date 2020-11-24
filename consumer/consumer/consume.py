from functools import partial
from time import sleep

import paho.mqtt.client as mqtt


# connect_callback(client, userdata, flags, reasonCode, properties)
def on_connect_subscribe(topic, client: mqtt.Client, userdata, flags, reasonCode, properties=None):
    print(f'on connect, subscribing to topic {topic}')
    client.subscribe(topic)


"""
TODO!
make variations on the on_message callback, that can:
- reverse the string
- turn it into uppercase
- turn it upside down (https://www.fileformat.info/convert/text/upside-down-map.htm)

with:
- lambda
- partial function
- message processor class
"""


def on_message_callback(client, userdata, message: mqtt.MQTTMessage):
    print(f"received message: \n{message.payload}")


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
