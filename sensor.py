#!/usr/bin/python3

from ev3dev.ev3 import *

while True:
    print("====================")
    print("Light1:")
    print(ColorSensor('in1').reflected_light_intensity)
    # print("Light2:")
    # print(ColorSensor('in2').value())