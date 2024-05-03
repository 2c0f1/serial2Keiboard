from adafruit_hid import keycode
import board
import time
import busio
import usb_hid
import digitalio
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

print('reiniciou')
uart = busio.UART(board.GP0, board.GP1, baudrate=115200)
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)
def sender():
    def printer():
            led.value = True
            print(data)
            #print(data[0])
            print("%02x " % (data[0]))
            print(char)
            uart.write(data)
            led.value = False
    while True:
     if uart.in_waiting:
        data = uart.readline()
        print(data)
        char = data.decode(11).strip()
        print(char)
        if char:
            ascii_code = ord(char)
            print(ascii_code)
            print(char)
            if 0 <= ascii_code <= 378:   
                if char.isupper():
                    printer()
                    keyboard_layout.write({char: [Keycode.SHIFT]})
                    
                else:
                    keyboard_layout.write(str(char))
                    printer()
                    
            elif char == "\r":  # Send space key
                    keyboard_layout.send(Keycode.ENTER)
                    printer()
            elif char == " ":  # Example: send Enter and Space keys simultaneously
                    keyboard_layout.send(Keycode.SPACE)
                    printer()    
            elif char == "\t":  
                    keyboard_layout.send(Keycode.TAB)
                    printer() 
            elif char == "\x1b[12~":  
                    keyboard_layout.send(Keycode.F2)
                    printer()                                 
sender()                                