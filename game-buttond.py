from mqtt.mqtt import MQTT
from board.board import Board
import time
import netifaces as ni
import json
import socket
from button.led_button import LedButton

led_button = LedButton(22, 18)


def status_message():
    b = Board()
    msg = {
        "board": b.get_board_id(),
        "ntpJitter": 99999,
        "timestamp": time.time(),
        "ip": ni.ifaddresses('bat0')[2][0]['addr'],
        "health": "not implemented",
        "validUntil": time.time() + 10
    }
    return msg


def button_message(state, id="main"):
    msg = {
        "id": id,
        "status": state,
        "timestamp": time.time()
    }
    return msg


def led_message(state, interval = False, color = False):
    msg = {
        "id": "main",
        "state": state
    }
    if interval:
        msg["interval"] = interval
    if color:
        msg["color"] = color
    return msg


def led_msg_handler(client: mqtt.Client, userdata, msg):
    data = json.loads(msg.payload)
    if data['state'] == "on":
        led_button.led_on()
    if data['state'] == "off":
        led_button.led_off()
    if data.['state'] == "blink":
        if data['interval']:
            led_button.led_blink_start(data['interval'])
        else:
            led_button.led_blink_start(200)

topics = [
    {
        "topic": "buttongame/global/led",
        "callback": led_msg_handler
    },
    {
        "topic": "buttongame/buttons/" + socket.gethostname() + "/led",
        "callback": led_msg_handler
    }
]

m = MQTT("mqtt.eclipse.org", topics)
m.mqttc.publish("buttongame/buttons/" + socket.gethostname() + "/led", led_message("blink"))

def button_handler(channel):
    m.mqttc.publish("buttongame/buttons/" + socket.gethostname() + "/button", button_message("pressed"))

led_button.register_pressed_callback(button_handler)

while True:
    time.sleep(1)