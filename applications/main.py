 #!/usr/bin/python
# -*- coding: UTF-8 -*-
# servo motor is connected to GPIO 2
#import chardet
import os
import sys 
import time
import RPi.GPIO as GPIO
from lib import lcd1_14driver
from PIL import Image,ImageDraw,ImageFont
import serial
import employee
import ultrasonic

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(2, GPIO.OUT)

servo = 2 # servo motor is connected to GPIO 2
GPIO.setup(servo,GPIO.OUT)


p=GPIO.PWM(servo,50)# 50hz frequency
p.start(2.5)# starting duty cycle ( it set the servo to 0 degree )


RST = 27
DC = 25
BL = 18
bus = 0 
device = 0

barcode = serial.Serial(port='/dev/ttyS0',baudrate = 9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)

font1 = ImageFont.truetype("font/Font00.ttf",21)
font2 = ImageFont.truetype("font/Font00.ttf",16)
font3 = ImageFont.truetype("font/Font02.ttf",25)

if not os.path.isfile("Library_books.txt"):  
    file=open('Library_books.txt',"a+")
    file.write("Today Books issue are :")
    file.write("\r")
    file.close()

disp = lcd1_14driver.LCD_1inch14()
disp.Init()
image2 = Image.new("RGB", (disp.width, disp.height), "WHITE")


image = Image.open('pic/sb.jpg')	
disp.ShowImage(image)


time.sleep(2)
disp.clear()
draw = ImageDraw.Draw(image2)

draw.text((40,5),"SCAN BOOKS ID", font = font1, fill = "BLUE")
disp.ShowImage(image2)

count = 30
while True:
    data = barcode.readline(14)#read data comming from pi barcode reader
    distance = ultrasonic.start()
    
    if distance <=30:
        GPIO.output(26, GPIO.HIGH)
        
        if data:
                dec_1 = data.decode("utf-8")#  convert data to string
                dec = dec_1.replace('\r', '')# replace this \r by ' '
                print(dec)
                feedback = employee.search(dec)# call the search from employee file
                if feedback == False:
                    print("Unauthorised access")
                    GPIO.output(26, GPIO.LOW)
                    p.ChangeDutyCycle(2.5)
                    draw.text((5,count),"Unauthorised access", font = font1, fill = "RED")
                    disp.ShowImage(image2)
                else:
                    print("Authorised access")
                    p.ChangeDutyCycle(7.5)
                    print(feedback)
                    GPIO.output(26, GPIO.HIGH)
                    draw.text((5,count),"Authorised access", font = font1, fill = "RED")
                    disp.ShowImage(image2)
                    time.sleep(2)
                    count += 25

                time.sleep(0.5)
    else:
        GPIO.output(26, GPIO.LOW)
        p.ChangeDutyCycle(2.5)
       


        
    
 
