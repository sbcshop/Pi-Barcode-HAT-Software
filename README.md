# Pi-Barcode-HAT

<img src= "https://github.com/sbcshop/Pi-Barcode-HAT/blob/main/images/img2.png" />
<img src= "https://github.com/sbcshop/Pi-Barcode-HAT/blob/main/images/img1.png" />

### Barcode HAT for Raspberry Pi is a robust and compact barcode scanner board that consists of a DE2120 scanner module, buzzer, 1.14” LCD screen, micro-USB port. It is designed to scan 20 different barcode symbologies in the segment of both 1D and 2D symbology like barcodes and QR codes.

### Enable the SPI first in raspberry pi, for this go to cmd then type ```sudo raspi-config``` then go to ->interface option -> SPI - YES

## Setup Pi Barcode HAT
First, you need to change the mode of the Pi Barcode HAT. Put Barcode HAT at the top of the raspberry pi, then you need to scan the below barcode settings before running the code 
 * Mode is TTL/RS232 (serial communication interface(UART)) for this you need to scan below the barcode, Connect USB to Barcode Hat For Raspberry Pi.
  
<img src= "https://github.com/sbcshop/Pi-Barcode-HAT/blob/main/images/ttl_rs232.JPG" />
   
 * Change the baud rate to (9600) for this you need to scan the below barcode by pressing the scan button on the Barcode Hat For Raspberry Pi.

 <img src= "https://github.com/sbcshop/Pi-Barcode-HAT/blob/main/images/baudrate.JPG" />

## Use Pi Barcode Hat without Raspberry Pi( Via USB Cable )
For this you need to scan below barcode settings

 <img src= "https://github.com/sbcshop/Pi-Barcode-HAT/blob/main/images/img7.JPG" />
  
  For USB COM Mode sacan below barcode
  
  <img src ="https://github.com/sbcshop/Pi-Barcode-HAT/blob/main/images/usb_com_mode.PNG" />
  
 <img src= "https://github.com/sbcshop/Pi-Barcode-HAT/blob/main/images/img5.JPG" />

## Working
<img src= "https://github.com/sbcshop/Pi-Barcode-HAT/blob/main/images/img6.JPG" />

## Applications
First of all, move all the files from the applications folder to the outside folder which is the Pi-Barcode-HAT folder, so that main.py could access the files in the lib sub-directory
* Pins of the ultrasonic sensor (we use this sensor to avoid pressing the push button to scan the barcode ), we use 3v ultrasonic sensor
   * Trig is connected to GPIO 4
   * Echo is connected to GPIO 17
* Servo motor
   * Servo motor pin is connected to GPIO 2

## Working of Applications 
  * Smart shopping
  <img src= "https://github.com/sbcshop/Pi-Barcode-HAT/blob/main/images/img1.JPG" />
  
  * Smart Library Management System
  <img src= "https://github.com/sbcshop/Pi-Barcode-HAT/blob/main/images/img4.JPG" />
  
  * Smart Attendence System
  <img src= "https://github.com/sbcshop/Pi-Barcode-HAT/blob/main/images/img2.JPG" />

 
 ## Documentation

* [Pi Barcode HAT Hardware](https://github.com/sbcshop/Pi-Barcode-HAT-Hardware)
* [Getting Started with Raspberry Pi](https://www.raspberrypi.com/documentation/computers/getting-started.html)
* [Raspberry Pi Pico Official website](https://www.raspberrypi.com/documentation/microcontrollers/)
* [Raspberry Pi Datasheet](https://www.raspberrypi.com/documentation/computers/compute-module.html)
* [Hardware Design](https://www.raspberrypi.com/documentation/computers/compute-module.html)
* [Raspberry Pi](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html)

## Related Products

* [Round LCD HAT](https://shop.sb-components.co.uk/products/round-lcd-hat-for-raspberry-pi?_pos=3&_sid=b3a6e03ae&_ss=r)

 ![Round LCD HAT](https://cdn.shopify.com/s/files/1/1217/2104/products/RaspberryPiRoundLCD.png?v=1619171155&width=400)


## Product License

This is ***open source*** product. Kindly check LICENSE.md file for more informnation.

Please contact [support@sb-components.co.uk](support@sb-components.co.uk) for technical support.
<p align="center">
  <img width="360" height="100" src="https://cdn.shopify.com/s/files/1/1217/2104/files/Logo_sb_component_3.png?v=1666086771&width=350">
</p>



