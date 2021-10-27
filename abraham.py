import time
import os
import sys
from pymycobot.mycobot import MyCobot
from pymycobot.genre import Angle, Coord

sys.path.append(os.path.dirname(__file__))
from port_setup import setup

reset = [153.19, 137.81, -153.54, 156.79, 87.27, 13.62]


def test(mycobot):
    print("\nStart check basic options\n")

    mycobot.set_color(255, 255, 0)
    print("::set_color() ==> color {}\n".format("255 255 0"))
    time.sleep(1)

    angles = [0, 0, 0, 90, 0, 0]
    #angles = [0, 0, 85, 0, 0, 90]
    mycobot.send_angles(angles, 15)
    print("::send_angles() ==> angles {}, speed 20\n".format(angles))
    time.sleep(4)

    #angles = [0, -90,100, 0, 0, 90]
    mycobot.send_angles(angles, 15)
    print("::send_angles() ==> angles {}, speed 20\n".format(angles))
    time.sleep(4)


    #angles = [0, -130,15, 122.5, 0, 90]
    mycobot.send_angles(angles, 15)
    print("::send_angles() ==> angles {}, speed 20\n".format(angles))
    time.sleep(4)

    #angles = [0, -90,15, 85, 0, 90]
    mycobot.send_angles(angles, 15)
    print("::send_angles() ==> angles {}, speed 20\n".format(angles))
    time.sleep(2)

    #mycobot.send_angle(Angle.J2.value, 15, 10)
    #print("::send_angle() ==> angle: joint1, degree: 90, speed: 50\n")
    #time.sleep(7)


    print("=== check end ===\n")


if __name__ == "__main__":
    print(
        """
--------------------------------------------
| This file will test basic option method: |
|     set_led_color()                      |
|     send_angles()                        |
|     get_angles()                         |
|     send_angle()                         |
|     send_radians()                       |
|     get_radians()                        |
|     send_coords()                        |
|     get_coords()                         |
|     send_coord()                         |
--------------------------------------------
          """
    )
    time.sleep(3)
    # port = subprocess.check_output(['echo -n /dev/ttyUSB*'],
    # shell=True).decode()
    # with open(os.path.dirname(__file__) + "/port.txt") as f:
        # port = f.read().strip().replace("\n", "")
        # print(port)
    mycobot = setup()
    test(mycobot)
