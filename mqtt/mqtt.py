import paho.mqtt.client as mqtt
import socket


class MQTT:
    def __init__(self, broker, topics: list):
        self.mqttc = mqtt.Client(client_id=socket.gethostname(), clean_session=True)
        self.topics = topics
        self.mqttc.on_connect = self.on_connect
        self.mqttc.on_message = self.on_message
        self.mqttc.connect(broker)
        self.mqttc.loop_start()

    def on_message(self, client: mqtt.Client, userdata, msg):
        print(msg.topic + " " + str(msg.payload))

    def on_connect(self, client: mqtt.Client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        for topic in self.topics:
            self.mqttc.subscribe(topic['topic'])
            if topic['callback']:
                self.mqttc.message_callback_add(topic['topic'], topic['callback'])

    def subscribe(self, topic):
        self.mqttc.subscribe(topic['topic'])
        self.mqttc.message_callback_add(topic['topic'], topic['callback'])
        if topic['callback']:
            self.topics += topic
