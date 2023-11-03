'''
This is the example code for scanning barcode 
Develop by Sb-components

'''
from PIL import Image,ImageDraw,ImageFont
from lib import Pi_barcode
import time
import sys

'''
* write this in command "dmesg" in cmd of raspberry pi and see the port
* if you use as HAT then your port is "ttyS0", 
* if you use as barcode hat via micro-usb then your port is ttyACM0,ttyACM1.... etc, 
* To see the working display, you will have to use the device as HAT. In USB mode display will not work.
'''

port = "/dev/ttyS0"  # write port here for eg.ttyS0,ttyACM0,ttyACM1.... etc
Baudrate = 115200    # write baudrate here

######## Choose font for lcd display ##############
font1 = ImageFont.truetype("font/Font00.ttf",25)
font2 = ImageFont.truetype("font/Font00.ttf",16)
font3 = ImageFont.truetype("font/Font02.ttf",25)
###################################################

barcode = Pi_barcode.Barcode_Scanner(port,Baudrate)

######################### LCD Part ################
disp = Pi_barcode.lcd_display()
disp.Init()
image = Image.new("RGB", (disp.width, disp.height), "WHITE")
image1 = Image.open('pic/sb.jpg')	
disp.ShowImage(image1)
time.sleep(1) # 1 sec delay
disp.clear()
draw = ImageDraw.Draw(image)
draw.text((20,5),"SCAN BARCODE", font = font1, fill = "BLUE")
disp.ShowImage(image)
#################################################

data = ""
print("\nScan the barcode!")
print("\n")
count= 30
while True:
        data = barcode.Read()
        if data:
            print("Data: " + str(data))
            draw.text((20,count),str(data), font = font1, fill = "RED")
            disp.ShowImage(image)
            data = ""
            count += 25
        time.sleep(0.05)

