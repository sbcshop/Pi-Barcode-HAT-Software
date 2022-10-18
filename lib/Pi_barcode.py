# zero_barcode.py
# Python liberay for Zero Barcode Scanner and LCD 1.14"

import serial
import time
import spidev
import numpy as np

class Lcd_config:
    #Zero Barcode HAT connected with following dedicated spi pins of Rpi 
    def __init__(self,spi=spidev.SpiDev(0,0),spi_freq=40000000,rst = 27,dc = 25,bl = 18,bl_freq=1000,i2c=None,i2c_freq=100000):
        import RPi.GPIO      
        self.np=np
        self.RST_PIN= rst
        self.DC_PIN = dc
        self.BL_PIN = bl
        self.SPEED  =spi_freq
        self.BL_freq=bl_freq
        self.GPIO = RPi.GPIO
        self.GPIO.setmode(self.GPIO.BCM)
        self.GPIO.setwarnings(False)
        self.GPIO.setup(self.RST_PIN,   self.GPIO.OUT)
        self.GPIO.setup(self.DC_PIN,    self.GPIO.OUT)
        self.GPIO.setup(self.BL_PIN,    self.GPIO.OUT)
        self.GPIO.output(self.BL_PIN,   self.GPIO.HIGH)        
        #Initialize SPI
        self.SPI = spi
        if self.SPI!=None :
            self.SPI.max_speed_hz = spi_freq
            self.SPI.mode = 0b00

    def digital_write(self, pin, value):
        self.GPIO.output(pin, value)

    def digital_read(self, pin):
        return self.GPIO.input(pin)

    def delay_ms(self, delaytime):
        time.sleep(delaytime / 1000.0)

    def spi_writebyte(self, data):
        if self.SPI!=None :
            self.SPI.writebytes(data)
    def bl_DutyCycle(self, duty):
        self._pwm.ChangeDutyCycle(duty)
        
    def bl_Frequency(self,freq):
        self._pwm.ChangeFrequency(freq)
           
    def module_init(self):
        self.GPIO.setup(self.RST_PIN, self.GPIO.OUT)
        self.GPIO.setup(self.DC_PIN, self.GPIO.OUT)
        self.GPIO.setup(self.BL_PIN, self.GPIO.OUT)
        self._pwm=self.GPIO.PWM(self.BL_PIN,self.BL_freq)
        self._pwm.start(100)
        if self.SPI!=None :
            self.SPI.max_speed_hz = self.SPEED        
            self.SPI.mode = 0b00     
        return 0

    def module_exit(self):
        if self.SPI!=None :
            self.SPI.close()
        
        self.GPIO.output(self.RST_PIN, 1)
        self.GPIO.output(self.DC_PIN, 0)        
        self._pwm.stop()
        time.sleep(0.001)
        self.GPIO.output(self.BL_PIN, 1)
        #self.GPIO.cleanup()


class lcd_display(Lcd_config):

    width = 240
    height = 135 
    def command(self, cmd):
        self.digital_write(self.DC_PIN, self.GPIO.LOW)
        self.spi_writebyte([cmd])
        
    def data(self, val):
        self.digital_write(self.DC_PIN, self.GPIO.HIGH)
        self.spi_writebyte([val])
        
    def reset(self):
        """Reset the display"""
        self.GPIO.output(self.RST_PIN,self.GPIO.HIGH)
        time.sleep(0.01)
        self.GPIO.output(self.RST_PIN,self.GPIO.LOW)
        time.sleep(0.01)
        self.GPIO.output(self.RST_PIN,self.GPIO.HIGH)
        time.sleep(0.01)
        
    def Init(self):
        """Initialize dispaly"""  
        self.module_init() #initialising lcd module
        self.reset()

        self.command(0x36)
        self.data(0x70)                 #self.data(0x00)

        self.command(0x3A) 
        self.data(0x05)

        self.command(0xB2)
        self.data(0x0C)
        self.data(0x0C)
        self.data(0x00)
        self.data(0x33)
        self.data(0x33)

        self.command(0xB7)
        self.data(0x35) 

        self.command(0xBB)
        self.data(0x19)

        self.command(0xC0)
        self.data(0x2C)

        self.command(0xC2)
        self.data(0x01)

        self.command(0xC3)
        self.data(0x12)   

        self.command(0xC4)
        self.data(0x20)

        self.command(0xC6)
        self.data(0x0F) 

        self.command(0xD0)
        self.data(0xA4)
        self.data(0xA1)

        self.command(0xE0)
        self.data(0xD0)
        self.data(0x04)
        self.data(0x0D)
        self.data(0x11)
        self.data(0x13)
        self.data(0x2B)
        self.data(0x3F)
        self.data(0x54)
        self.data(0x4C)
        self.data(0x18)
        self.data(0x0D)
        self.data(0x0B)
        self.data(0x1F)
        self.data(0x23)

        self.command(0xE1)
        self.data(0xD0)
        self.data(0x04)
        self.data(0x0C)
        self.data(0x11)
        self.data(0x13)
        self.data(0x2C)
        self.data(0x3F)
        self.data(0x44)
        self.data(0x51)
        self.data(0x2F)
        self.data(0x1F)
        self.data(0x1F)
        self.data(0x20)
        self.data(0x23)
        
        self.command(0x21)

        self.command(0x11)

        self.command(0x29)
  
    def SetWindows(self, Xstart, Ystart, Xend, Yend):
        #set the X coordinates
        self.command(0x2A)
        self.data((Xstart+40)>>8& 0xff) #Set the horizontal starting point to the high octet
        self.data((Xstart+40)   & 0xff) #Set the horizontal starting point to the low octet
        self.data((Xend-1+40)>>8& 0xff) #Set the horizontal end to the high octet
        self.data((Xend-1+40)   & 0xff) #Set the horizontal end to the low octet 
        
        #set the Y coordinates
        self.command(0x2B)
        self.data((Ystart+53)>>8& 0xff) #Set the vertical starting point to the high octet
        self.data((Ystart+53)   & 0xff) #Set the vertical starting point to the low octet
        self.data((Yend-1+53)>>8& 0xff) #Set the vertical end to the high octet
        self.data((Yend-1+53)   & 0xff) #Set the vertical end to the low octet

        self.command(0x2C) 
        
    def ShowImage(self,Image):
        """Set buffer to value of Python Imaging Library image."""
        """Write display buffer to physical display"""
                
        imwidth, imheight = Image.size
        if imwidth != self.width or imheight != self.height:
            raise ValueError('Image must be same dimensions as display \
                ({0}x{1}).' .format(self.width, self.height))
        img = self.np.asarray(Image)
        pix = self.np.zeros((self.height,self.width,2), dtype = self.np.uint8)
        
        pix[...,[0]] = self.np.add(self.np.bitwise_and(img[...,[0]],0xF8),self.np.right_shift(img[...,[1]],5))
        pix[...,[1]] = self.np.add(self.np.bitwise_and(self.np.left_shift(img[...,[1]],3),0xE0),self.np.right_shift(img[...,[2]],3))
        
        pix = pix.flatten().tolist()
        self.SetWindows ( 0, 0, self.width, self.height)
        self.digital_write(self.DC_PIN,self.GPIO.HIGH)
        for i in range(0,len(pix),4096):
            self.spi_writebyte(pix[i:i+4096])		
            
    def clear(self):
        """Clear contents of image buffer"""
        _buffer = [0xff]*(self.width * self.height * 2)
        self.SetWindows ( 0, 0, self.width, self.height)
        self.digital_write(self.DC_PIN,self.GPIO.HIGH)
        for i in range(0,len(_buffer),4096):
            self.spi_writebyte(_buffer[i:i+4096])      
        

class Barcode_Scanner(object):    
    # DE2120 response
    ACKN_CMD = 0x06 #sending acknowledge command to check zero barcode status
    NACK_CMD = 0x15

    # Constructor
    def __init__(self, port,Baud_rate):
        self.port = port
        self.baud_rate = Baud_rate
        if port is not None:
            self.port = serial.Serial(port, Baud_rate, timeout=1)
        else:
            self.port = port
        
    # Construct a command/parameter and send it to the module.
    def send_command(self, cmd):
        # start = '^_^'
        # end   = '.'
        command_string = '^_^'+ cmd +'.'
        self.port.write(command_string.encode())       
        ack_value = self.port.read()
        if ord(ack_value) == 0x06:
            return True
        elif ord(ack_value) == 0x15:
            return False
        return False
    
    def begin(self):
        if self.Connected() == False:
            return False
        self.port.flush()
        return True
    
    # determine whether the module is connected.
    def Connected(self):   
        String = "^_^" + chr(4) + "SPYFW."
        self.port.write(String.encode())
        
        # If it's an ACKN, return true
        # Otherwise, return false
        ack_value = self.port.read()
        if ord(ack_value) == 0x06:   # ACKN
            return True
        elif ord(ack_value) == 0x15: # NACK
            return False
        else:
            return False
        
    # Change the serial baud rate for the barcode module
    def Select_baudrate(self, baud_rate):
        if baud_rate == 1200:
            return self.send_command("232BAD2")# at 1200 baudrate
            
        elif baud_rate == 2400:
            return self.send_command("232BAD3") #for setting baudrate at 2400

        elif baud_rate == 4800:
            return self.send_command("232BAD4") #for setting baudrate at 4800

        elif baud_rate == 9600:
            return self.send_command("232BAD5") #for setting baudrate at 9600

        elif baud_rate == 19200:
            return self.send_command("232BAD6") #for setting baudrate at 19200

        elif baud_rate == 38400:
            return self.send_command("232BAD7") #for setting baudrate at 38400

        elif baud_rate == 57600:
            return self.send_command("232BAD8") #for setting baudrate at 57600
        
        else:   
            return self.send_command("232BAD9") # for Default (115200) baudrate
    
    # Returns the number of bytes in the serial receive buffer
    def available(self):
        return self.port.in_waiting

    # read byte from the serial port
    def read(self):
        return self.port.read()
    
    # Start reading when in trigger mode (default)
    def start_scan(self):
        return self.send_command("SCAN")
      
    # Stop reading when in trigger mode. Module will automatically
    def stop_scan(self):
        return self.send_command("SLEEP")
      
    
    # Check the receive buffer for serial data from the barcode scanner
    def Read(self):
        # Check if there's data available
        if self.port.in_waiting == False:
            return False
        
        # read from serial port
        ack_value = self.port.read_until()
        return ack_value.decode()
    
    # Change the beep frequency between low, med, and high
    def Select_buzzer_sound(self, sound):
        if sound == 0:
            return self.send_command("BEPPWM0") #buzzer freq at Active Drive
        elif sound == 1:
            return self.send_command("BEPPWM1") # Low freq (Passive)
        elif sound == 2:
            return self.send_command("BEPPWM2") #Medium freq (default)        

        elif sound == 3:
            return self.send_command("BEPPWM3") #High freq (Passive)
        return False



    # Enable buzzer beep on module startup
    def Boot_beep_sound_enable(self):
        return self.send_command("BEPPWR1") #beep sound enabled during boot
    
    # Disable buzzer beep on module  startup
    def Boot_beep_sound_disable(self):
        return self.send_command("BEPPWR0") #beep sound disbled during boot
    
    # Enable buzzer beep on successful read
    def Enable_buzzer_beep_sound(self):
        return self.send_command("BEPSUC1") #beep sound enabled on successfull read
    
    # Disable buzzer beep on successful read
    def Disable_buzzer_beep_sound(self):
        return self.send_command("BEPSUC0") #beep sound disabled on successfull read
     
    # Turn white illumination LED on
    def White_light_on(self):
        return self.send_command("LAMENA1") #turning white light ON
    
    # Turn white illumination LED off
    def White_light_off(self):
        return self.send_command("LAMENA0") #white light turning OFF
        
    # Turn red scan line on
    def Red_light_on(self):
        return self.send_command("AIMENA1") #red scan line enabled
    
    # Turn red scan line off
    def Red_light_off(self):
        return self.send_command("AIMENA0") #red scan line disabled

    # Enable decoding of all 1D symbologies
    def On_1D_mode(self):
        return self.send_command("ODCENA")
    
    # Disable decoding of all 1D symbologies
    def Off_1D_mode(self):
        return self.send_command("ODCDIS")

    # Enable decoding of all 2D symbologies
    def On_2D_mode(self):
        return self.send_command("AQRENA")
        
    # Disable decoding of all 2D symbologies
    def Off_2D_mode(self):
        return self.send_command("AQRDIS")
    
    # Change the percentage of the frame to scan for barcodes
    def Area_of_reading_change(self, percent):
        if percent == 80:
            return self.send_command("IMGREG1") # IMGREG1 - Center 80%

        elif percent == 60:
            return self.send_command("IMGREG2") # IMGREG2 - Center 60%

        elif percent == 40:
            return self.send_command("IMGREG3") # IMGREG3 - Center 40%

        elif percent == 20:
            return self.send_command("IMGREG4") # IMGREG4 - Center 20%

        else:   # Default to scanning 100% of the area
            return self.send_command("IMGREG0") # IMGREG0 - Full Width (default)     
    
    # Enable mirror image reading as defined in the DE2120 Settings Manual
    def Enable_mirror_image(self):
        return self.send_command("MIRLRE1")
    
    # Disable mirror image reading as defined in the DE2120 Settings Manual
    def Disable_mirror_image(self):
        return self.send_command("MIRLRE0")
   
    # Enable USB communication and set the mode
    # THIS WILL MAKE THE MODULE UNRESPONSIVE ON TTL
    def USB_Communication_mode(self, mode):
        if mode == 0:
            return self.send_command("PORKBD") # USB-KBW Mode

        elif mode == 0:
            return self.send_command("PORHID") # USB-HID Mode
        
        elif mode == 0:
            return self.send_command("PORVIC") # USB-COM Mode 
        
        elif mode == 0:
            return self.send_command("POR232") # RS232/TTL        
        return False
    
    # Enable continuous reading mode and set the interval for same-code reads
    def Enable_continous_read_mode(self, interval = 2):
        if interval == 0:
            self.send_command("SCMCNT") # Continuous            
            time.sleep(0.01)          
            return self.send_command("CNTALW0") # Output Once

        if interval == 1:
            self.send_command("SCMCNT") # Continuous            
            time.sleep(0.01) 
            return self.send_command("CNTALW1") # Output Continuous No Interval
        
        if interval == 2:
            self.send_command("SCMCNT") # Continuous            
            time.sleep(0.01)
            return self.send_command("CNTALW2") # Output Continuous 0.5s Interval
        
        if interval == 3:
            self.send_command("SCMCNT") # Continuous            
            time.sleep(0.01)          
            return self.send_command("CNTALW3") # Output Continuous 1s Interval
        
        return False
    
    # Disable the motion sensitive and continuous read mode.
    # Return to the default trigger mode.
    def Manual_mode_on(self,mode):
        if mode == 0:
            return self.send_command("SCMMAN") # Manual (default)

        elif mode == 1:
            return self.send_command("SCMCNT") # Continuous

        elif mode == 2:
            return self.send_command("SCMMDH") # Motion Mode
        else:
            return False

    # Enable the motion sensitive read mode.
    def turn_on_motion_sense(self, s = 20):
        if s == 15:
            self.send_command("SCMMDH") 
            time.sleep(0.01)
            return self.send_command("MDTTHR15") #sensitivity is extremely high
        
        elif s == 20:
            self.send_command("SCMMDH")
            time.sleep(0.01)
            return self.send_command("MDTTHR20") #for high sensitivity(default)
        
        elif s == 30:
            self.send_command("SCMMDH")
            time.sleep(0.01)
            return self.send_command("MDTTHR30") #for highish sensitivity
        
        elif s == 50:
            self.send_command("SCMMDH")
            time.sleep(0.01)
            return self.send_command("MDTTHR50") #for medium sensitivity

        elif s == 100:
            self.send_command("SCMMDH")
            time.sleep(0.01)
            return self.send_command("MDTTHR100") #for low sensitivity
        return False

    # disconnect the module from the serial port
    def Reset_factory(self):
        return self.send_command("DEFALT") #All settings will be on default 
