#!/usr/bin/python
# Trigger is connected to raspberry pi GPIO 4, echo is connected to GPIO 17
import RPi.GPIO as GPIO
import time

def start():
           #try:
            GPIO.setmode(GPIO.BCM)
            #GPIO.setmode(GPIO.BOARD)
            GPIO.setwarnings(False)
            PIN_TRIGGER = 4 #GPIO 4
            PIN_ECHO = 17   # GPIO 17

            GPIO.setup(PIN_TRIGGER, GPIO.OUT)
            GPIO.setup(PIN_ECHO, GPIO.IN)

            GPIO.output(PIN_TRIGGER, GPIO.LOW)

            #print ("Waiting for sensor to settle")

            time.sleep(0.2)

            #print ("Calculating distance")

            GPIO.output(PIN_TRIGGER, GPIO.HIGH)

            time.sleep(0.00001)

            GPIO.output(PIN_TRIGGER, GPIO.LOW)

            while GPIO.input(PIN_ECHO)==0:
                  pulse_start_time = time.time()
            while GPIO.input(PIN_ECHO)==1:
                  pulse_end_time = time.time()

            pulse_duration = pulse_end_time - pulse_start_time
            distance = round(pulse_duration * 17150, 2)
            #print ("Distance:",distance,"cm")
            return distance

            #finally:
                  #GPIO.cleanup()
