
from ev3dev.ev3 import *
import sys
m = LargeMotor('outA')
m.run_forever(speed_sp=500)
m.run_timed(time_sp=300, speed_sp=-300)
m.stop()