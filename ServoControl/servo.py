#Example from https://gpiozero.readthedocs.io/en/stable/api_output.html#servo
# https://www.digikey.com/en/maker/tutorials/2021/how-to-control-servo-motors-with-a-raspberry-pi#:~:text=This%20simple%20python%20script%20first,waits%20for%20half%20a%20second
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
