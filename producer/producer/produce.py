import itertools
from functools import partial
from time import sleep

import paho.mqtt.client as mqtt

SLEEP_TIME = 30


# def on_disconnect(client, userdata, rc)
def disconnect_callback(host: str, port: str, client: mqtt.Client, userdata, rc):
    print("reconnecting...")
    print(userdata)
    print(rc)
    client.connect(host, port)


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
    auto_reconnect = partial(disconnect_callback, host, port)
    client.on_disconnect = auto_reconnect
    counter = itertools.count()
    while True:
        c = next(counter)
        print(c)
        client.publish(topic, f"Hello no. {c}")
        sleep(SLEEP_TIME)
