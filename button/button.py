try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")


class Button:
    def __init__(self, pin):
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self.pin = pin

    def is_pressed(self):
        return GPIO.input(self.pin)

    def register_pressed_callback(self, func, bounce=200):
        GPIO.add_event_detect(self.pin, GPIO.FALLING)
        GPIO.add_event_callback(self.pin, func, bouncetime=bounce)

    def unregister_all_callbacks(self):
        GPIO.remove_event_detect(self.pin)