from gpiozero import Robot
from time import sleep

robot = Robot(left=(7,8), right=(9,10))

for i in range(4):
  robot.forward()
  time.sleep(0.5)
  robot.right()
  time.sleep(0.25)