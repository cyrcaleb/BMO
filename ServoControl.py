from time import *
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

kit.servo[0].angle = 100
kit.servo[1].angle = 130

sleep(10)

while True:
  kit.servo[0].angle = 180
  kit.servo[1].angle = 30
  
  sleep(3)
  
  kit.servo[0].angle = 100
  kit.servo[1].angle = 130
  
  sleep(3)
  
  kit.servo[0].angle = 180
  
  sleep(1)
  
  kit.servo[1].angle = 30
  
  sleep(1)
  
   kit.servo[1].angle = 130
  
  sleep(1)
  
  kit.servo[0].angle = 100
  
  sleep(5)
  
  kit.servo[0].angle = 100
  kit.servo[1].angle = 30
  
  sleep(1)
  
  kit.servo[0].angle = 180
  kit.servo[1].angle = 130
  
  sleep(1)
  
  kit.servo[0].angle = 100
  kit.servo[1].angle = 30
  
  sleep(3)
  
  kit.servo[0].angle = 130
  
  sleep(5)
    
    
  
