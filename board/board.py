try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")


class Board:
    def __init__(self):
        self.id_pins = []
        self.id_pins.append({"pin": 6, "value": 1})
        self.id_pins.append({"pin": 12, "value": 2})
        self.id_pins.append({"pin": 13, "value": 4})
        self.id_pins.append({"pin": 16, "value": 8})
        self.id_pins.append({"pin": 19, "value": 16})
        self.id_pins.append({"pin": 20, "value": 32})
        self.id_pins.append({"pin": 21, "value": 64})
        self.id_pins.append({"pin": 26, "value": 128})
        self.id = 0

        for pin in self.id_pins:
            GPIO.setup(pin['pin'], GPIO.IN)

        self.get_board_id()

    def get_board_id(self):
        for pin in self.id_pins:
            if GPIO.input(pin['pin']):
                self.id += pin['value']
        return self.id