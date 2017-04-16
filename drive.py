
class PCA9685_Controller:
    def __init__(self, channel, frequency=60):
        import Adafruit_PCA9685
        # Initialize the PCA9685 using the default address (0x40).
        self.pwm = Adafruit_PCA9685.PCA9685()

        self.pwm.set_pwm_frequency(frequency)
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

        self.controller.set_pulse(throttle)

    
