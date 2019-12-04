from mqtt.mqtt import MQTT
from board.board import Board
import time
import netifaces as ni

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


def button_message():
    msg = {
        "id": "main",
        "status": "pressed",
        "timestamp": time.time()
    }


def led_message():
    msg = {
        "id": "main",
        "state": "on",
        "interval": 200,
        "color": "CAFEE"
    }

m = MQTT("mqtt.eclipse.org", [{"topic": "KIT/123", "callback": blubb}, {"topic": "KIT/#"}])

while True:
    time.sleep(1)