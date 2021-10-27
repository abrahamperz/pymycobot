import re
import sys
import os

velocity = 15
port = "MyCobot('/dev/ttyUSB5') \n"

if os.path.exists("run.py"):
    os.remove("run.py")

if os.path.exists("parse.txt"):
    os.remove("parse.txt")

if os.path.exists("tmp"):
    os.remove("tmp")

pattern = "MoveL"

file = open("3points.txt", "r")
for line in file:
    if re.search(pattern, line):
        file1 = open("parse.txt", "a")
        file1.writelines(line)
        file1.close()

file2 = open("run.py", "a")
file2.writelines("from pymycobot.mycobot import MyCobot\n")
file2.writelines("import time\n")
file2.writelines("import os\n")
file2.writelines("import sys\n")
file2.writelines("from pymycobot.mycobot import MyCobot\n")
file2.writelines("from pymycobot.genre import Angle, Coord\n")
file2.writelines("\n")
file2.writelines("sys.path.append(os.path.dirname(__file__))\n")
file2.writelines("from port_setup import setup\n")
file2.writelines("reset = [153.19, 137.81, -153.54, 156.79, 87.27, 13.62]\n\n")

def generate(new):
    var = new
    new = line.split()
    #print(new)
    x1 = new[0]; x1 = x1[11:len(x1)-1]
    x2 = new[1]; x2 = x2[0:len(x2)-1]
    x3 = new[2]; x3 = x3[0:len(x3)-1]
    x4 = new[3]; x4 = x4[0:len(x4)-1]
    x5 = new[4]; x5 = x5[0:len(x5)-1]
    x6 = new[5]; x6 = x6[0:len(x6)-3]
    #print(x1,x2,x3,x4,x5,x6)
    file2.writelines("  angles = ["+ x1 + "," + x2 + "," + x3 + "," + x4 + "," + x5 + "," + x6 + "]," + str(velocity) + ")\n")
    file2.writelines("  mycobot.send_angles(angles, 15) \n")
    #file2.writelines("print('::send_angles() ==> angles {}, speed 20\n'.format(angles)) \n")
    file2.writelines("  time.sleep(4) \n \n")


file2.writelines("def test(mycobot):\n")
with open("parse.txt", "r") as filew:
     for line in filew:
         new = line.split()
    #     file2.writelines(new)
        #print(new)
         generate(new)


file2.writelines("mycobot = setup()  \n")
file2.writelines("test(mycobot)  \n")

file2.close()
os.remove("parse.txt")
#uncomment next line, with the robot connected
#os.system('python3 run.py')
