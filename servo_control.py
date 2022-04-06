import pigpio
import sys
import time


class GroveServo:
    MIN_DEGREE = 0
    MAX_DEGREE = 180
    INIT_DUTY = 2.5

    def __init__(self, channel):
        self.channel = channel
        self.IO = pigpio.pi()
        self.IO.set_mode(channel, pigpio.OUTPUT)
        self.IO.set_PWM_frequency(channel, 50)
        self.IO.set_servo_pulsewidth(self.channel, 500)

    def __del__(self):
        self.IO.set_PWM_dutycycle(self.channel, 0)
        self.IO.set_PWM_frequency(self.channel, 0)

    def close(self):
        self.IO.set_servo_pulsewidth(self.channel, 1500)

    def open(self):
        self.IO.set_servo_pulsewidth(self.channel, 500)
        time.sleep(5)
        self.close()
        return 1


Grove = GroveServo


def main():
    if len(sys.argv) < 2:
        print('Usage: {} servo_channel'.format(sys.argv[0]))
        sys.exit(1)

    servo = GroveServo(int(sys.argv[1]))

    servo.close()
    time.sleep(1)
    servo.open()
    time.sleep(1)
    servo.close()


if __name__ == '__main__':
    main()
