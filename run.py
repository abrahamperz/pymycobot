from pymycobot.mycobot import MyCobot
import time
import os
import sys
from pymycobot.mycobot import MyCobot
from pymycobot.genre import Angle, Coord

sys.path.append(os.path.dirname(__file__))
from port_setup import setup
reset = [153.19, 137.81, -153.54, 156.79, 87.27, 13.62]

def test(mycobot):
  angles = [90,0,0,0,0,0]
  mycobot.send_angles(angles,15)
  time.sleep(4)
  angles = [0,0,0,90,0,0]
  mycobot.send_angles(angles,15)
  time.sleep(4)
  angles = [0,90,0,0,0,0]
  mycobot.send_angles(angles,15)
  time.sleep(4)
mycobot = setup()  
test(mycobot)  
