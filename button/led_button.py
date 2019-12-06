try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

from button.button import Button
import threading
import time


class LedButton(Button):
    def __init__(self, button_pin, led_pin):
        Button.__init__(button_pin)
        GPIO.setup(led_pin, GPIO.OUT)
        GPIO.output(led_pin, GPIO.LOW)
        self.led_pin = led_pin
        self.blink = None

    def led_on(self):
        GPIO.output(self.led_pin, GPIO.HIGH)

    def led_off(self):
        GPIO.output(self.led_pin, GPIO.LOW)

    def led_toggle(self):
        GPIO.output(self.led_pin, not GPIO.input(self.led_pin))

    def led_blink_start(self, duty):
        self.blink = BlinkLed(duty, self.led_pin)
        self.blink.start()

    def led_blink_stop(self):
        self.blink.stop()


class BlinkLed(threading.Thread):
    def __init__(self, duty, pin):
        threading.Thread.__init__(self)
        self.ended = False
        self.duty = duty
        self.pin = pin

    def run(self):
        while not self.ended:
            GPIO.output(self.pin, not GPIO.input(self.pin))
            time.sleep(self.duty/1000)

    def stop(self):
        self.ended = True
