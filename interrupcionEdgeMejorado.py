#!/usr/bin/env python3

from time import sleep
import RPi.GPIO as GPIO

pulsadorGPIORojo = 16
pulsadorGPIOVerde = 20

ledRojo = 2
ledVerde = 3

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pulsadorGPIORojo, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(pulsadorGPIOVerde, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(ledRojo, GPIO.OUT)
    GPIO.setup(ledVerde, GPIO.OUT)
    
    ledVerdeState = False
    ledRojoState = False

    while True:
        if ( GPIO.wait_for_edge(pulsadorGPIORojo, GPIO.BOTH,10)):
            print("PREDDES")
            if not (GPIO.input(pulsadorGPIORojo)):
                GPIO.output(ledRojo, GPIO.HIGH)
            else:
                GPIO.output(ledRojo, GPIO.LOW)
        
        elif (GPIO.wait_for_edge(pulsadorGPIOVerde, GPIO.BOTH,10)):
            if not ( GPIO.input(pulsadorGPIOVerde)):
                if (ledVerdeState):
                    ledVerdeState = False
                    GPIO.output(ledVerde, GPIO.LOW)
                else:
                    ledVerdeState = True
                    GPIO.output(ledVerde, GPIO.HIGH)
        else:
            print("H")
