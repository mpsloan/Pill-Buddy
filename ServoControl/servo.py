#Example from https://gpiozero.readthedocs.io/en/stable/api_output.html#servo
from gpiozero import Servo
from time import sleep

servo = Servo(17)

while True:
    servo.min()
    sleep(1)
    servo.mid()
    sleep(1)
    servo.max()
    sleep(1)
