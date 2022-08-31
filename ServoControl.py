from time import *
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

kit.servo[0].angle = 0
kit.servo[1].angle = 0

sleep(10)

while True:
  kit.servo[0].angle = 90
  kit.servo[1].angle = 90
  
  sleep(3)
  
  kit.servo[0].angle = 0
  kit.servo[1].angle = 0
  
  sleep(3)
  
  kit.servo[0].angle = 90
  
  sleep(1)
  
  kit.servo[1].angle = 90
  
  sleep(1)
  
   kit.servo[0].angle = 0
  
  sleep(1)
  
  kit.servo[1].angle = 0
  
  sleep(5)
  
  kit.servo[0].angle = 90
  kit.servo[1].angle = 0
  
  sleep(1)
  
  kit.servo[0].angle = 0
  kit.servo[1].angle = 90
  
  sleep(1)
  
  kit.servo[0].angle = 90
  kit.servo[1].angle = 0
  
  sleep(3)
  
  kit.servo[0].angle = 0
  
  sleep(5)
    
    
  
