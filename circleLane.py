#!/usr/bin/python3

from ev3dev.ev3 import *

def goStraight():
    LargeMotor('outA').run_timed(time_sp=300, speed_sp=1000)
    LargeMotor('outB').run_timed(time_sp=300, speed_sp=1000)

def turn():
    LargeMotor('outA').run_timed(time_sp=300, speed_sp=-300)
    LargeMotor('outB').run_timed(time_sp=300, speed_sp=300)

while True:
    light = ColorSensor('in1').value()
    if light > 50:
        turn()
    else:
        goStraight()