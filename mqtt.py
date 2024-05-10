import paho.mqtt.client as paho
import os
import json
import time
from datetime import datetime

ACCESS_TOKEN =""
broker="demo.thingsboard.io"
port=1883

def on_publish(client, userdata, result):
    print("data published to thingsboard\n")
    pass

client = paho.Client("control1")
client.on_publish = on_publish

client.useranme_pw_set(ACCESS_TOKEN)
client.connect(broker, port, keepalive=60)

while True:
    payload="{"
    payload+="\"Humidity\":60,";
    payload+="\"Temperature\":25,";
    payload+="}"

    ret=client.publish("v1/devices/me/telemetry", payload)
    print("Please check LATEST TELEMETRY field of your device")
    print(payload);
    time.sleep(5)
