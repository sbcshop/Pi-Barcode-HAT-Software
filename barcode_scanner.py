import RPi.GPIO as GPIO
import time
import serial
import os
from lib import lcd1_14driver
from PIL import Image,ImageDraw,ImageFont


RST = 27
DC = 25
BL = 18
bus = 0 
device = 0

barcode = serial.Serial(port='/dev/ttyS0',baudrate = 9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)

font1 = ImageFont.truetype("font/Font00.ttf",25)
font2 = ImageFont.truetype("font/Font00.ttf",16)
font3 = ImageFont.truetype("font/Font02.ttf",25)

if not os.path.isfile("present_students.txt"):  
    file=open('present_students.txt',"a+")
    file.write("Today Present Student are :")
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

draw.text((20,5),"SCAN BARCODE", font = font1, fill = "BLUE")
disp.ShowImage(image2)

count= 30
while 1:
        data = barcode.readline(14)#read data comming from pi barcode reader
        print(data)
        if data:
                dec_1 = data.decode("utf-8")#  convert data to string
                dec = dec_1.replace('\r', '')# replace this \r by ' '
                print(dec)
                draw.text((20,count),str(dec), font = font1, fill = "RED")
                disp.ShowImage(image2)
                count += 25
















                     
 
