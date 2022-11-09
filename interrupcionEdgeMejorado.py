#!/usr/bin/env python3

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

    while True:
        GPIO.wait_for_edge(pulsadorGPIORojo, GPIO.BOTH)
        i+=1
        print(f"El boton se ha pulsado {i}")

