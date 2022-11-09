#!/usr/bin/env python3

import signal
import sys
import RPi.GPIO as GPIO

pulsadorGPIORojo = 16
pulsadorGPIOVerde = 20

ledRojo = 2
ledVerde = 3

def callbackSalir (senial, cuadro): # señal y estado cuando se produjo la interrup.
    GPIO.cleanup () # limpieza de los recursos GPIO antes de salir
    sys.exit(0)

def callbackBotonPulsadoRojo (canal):
    global ledRojoState
    print("El boton se ha pulsado rojo")
    if (ledRojoState):
        ledRojoState = False
        GPIO.output(ledRojo, GPIO.LOW)
    else:
        ledRojoState = True
        GPIO.output(ledRojo, GPIO.HIGH)
        
def callbackBotonPulsadoVerde (canal):
    global ledVerdeState
    print("El boton se ha pulsado verde")
    if (ledVerdeState):
        ledVerdeState = False
        GPIO.output(ledVerde, GPIO.LOW)
    else:
        ledVerdeState = True
        GPIO.output(ledVerde, GPIO.HIGH)

if __name__ == '__main__':

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pulsadorGPIORojo, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(pulsadorGPIOVerde, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(ledRojo, GPIO.OUT)
    GPIO.setup(ledVerde, GPIO.OUT)

    ledRojoState = False
    ledVerdeState = False

    GPIO.add_event_detect(pulsadorGPIORojo, GPIO.BOTH, 
      callback=callbackBotonPulsadoRojo, bouncetime=5) # expresado en ms.

    GPIO.add_event_detect(pulsadorGPIOVerde, GPIO.BOTH, 
      callback=callbackBotonPulsadoVerde, bouncetime=5) # expresado en ms.
    
    signal.signal(signal.SIGINT, callbackSalir) # callback para CTRL+C
    signal.pause() # esperamos por hilo/callback CTRL+C antes de acabar

