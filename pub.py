import random
import time
import sys
import json
import datetime
from paho.mqtt import client as mqtt_client

args = sys.argv
broker = args[1]                 #broker.emqx.io
port = int(args[2])                   #1883
repetition = int(args[3])
use_file = args[4]
data = json.load(open(use_file,'r'))
topic = 'device/' + data["topic_typ"]
client_id = f'publish-{random.randint(0, 1000)}'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish(client):
    msg_count = 1
    while True:
        time.sleep(0.1)
        # create_dummy_data()
        insert_timestamp()
        msg = json.dumps(data)
        result = client.publish(topic, msg)
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1
        if msg_count > repetition:
            break

def insert_timestamp():
    data["timestamp"] = str(datetime.datetime.now())

# def create_dummy_data():
    


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)
    client.loop_stop()

if __name__ == '__main__':
    run()