
class PCA9685_Controller:
    def __init__(self, channel, frequency=60):
        import Adafruit_PCA9685
        # Initialize the PCA9685 using the default address (0x40).
        self.pwm = Adafruit_PCA9685.PCA9685()

        self.pwm.set_pwm_freq(frequency)
        self.channel = channel

    def set_pulse(self, pulse):
        self.pwm.set_pwm(self.channel, 0, pulse)


class PWMSteeringActuator:
    #LEFT_ANGLE = -1
    #RIGHT_ANGLE = 1

    def __init__(self, controller = None, left_pulse = 290, right_pulse = 490):
        self.controller = controller
        #self.left_pulse = left_pulse
        #self.right_pulse = right_pulse

    def update(self, angle):

        self.controller.set_pulse(angle)

class PWMThrottleActuator:

    def __init__(self, controller=None, max_pulse=300, min_pulse=490, zero_pulse=350):
        self.controller = controller
        self.max_pulse = max_pulse
        self.min_pulse = min_pulse
        self.zero_pulse = zero_pulse
        #self.calibrate()

    def update(self, throttle):
        sys.stdout.flush()
        self.controller.set_pulse(throttle)

import sys, termios, tty, os, time

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
button_delay = 0.2




throttle_controller = PCA9685_Controller(channel = 0)    
steering_controller = PCA9685_Controller(channel = 1)

my_throttle = PWMThrottleActuator(controller = throttle_controller)
my_steering = PWMSteeringActuator(controller = steering_controller)

counter = 0
while True:
    
    char = getch()
    #throttle_controller.set_pulse(350)
    if(char == "a"):
        my_steering.update(480)
    elif(char == "d"):
        my_steering.update(350)
    elif(char == "w" and counter == 0):
        print("char = w, counter = " + str(counter) + ", throttle = 370")
        my_throttle.update(370)
        counter += 1
    elif(char == "w" and counter == 1):
        print("char = w, counter = 1, throttle = 400")
        my_throttle.update(400)
        counter -= 1
    elif(char == "s"):
        my_steering.update(410)
    elif(char == "x"):
        break

