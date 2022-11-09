#!/usr/bin/env python3

import time
import RPi.GPIO as GPIO

pulsadorGPIORojo = 16
pulsadorGPIOVerde = 20

ledRojo = 2
ledVerde = 3

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)

    # Activamos resistencia pull_up_down en modo HIGH, esto es:
    # - HIGH: estado por defecto del GPIO (no se ha pulsado).
    # - LOW: estado del GPIO cuando se ha pulsado el boton.
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pulsadorGPIORojo, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(pulsadorGPIOVerde, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(ledRojo, GPIO.OUT)
    GPIO.setup(ledVerde, GPIO.OUT)

    pulsado = False

    while True:
        if not GPIO.input(pulsadorGPIORojo): # la lectura siempre da 1 (HIGH/True) excepto al pulsar, y solo en ese instante, que da 0 (LOW/False)
            if not pulsado: # con esta variable evitamos considerar más de una vez una pulsación;
                            # puede que se lea +1 vez el estado del pin antes de cambiar su estado
                            # Este fenómeno se conoce como rebote (o bounce). Algunas funciones
                            # permiten establecer un parámetro denominado "bouncetime"
                print("El boton se ha pulsado")
                GPIO.output(ledRojo, GPIO.HIGH)
                pulsado = True
        elif not GPIO.input(pulsadorGPIOVerde):
            if not pulsado: # con esta variable evitamos considerar más de una vez una pulsación;
                # puede que se lea +1 vez el estado del pin antes de cambiar su estado
                # Este fenómeno se conoce como rebote (o bounce). Algunas funciones
                # permiten establecer un parámetro denominado "bouncetime"
                print("El boton se ha pulsado")
                GPIO.output(ledVerde, GPIO.HIGH)
                pulsado = True
        else:
            GPIO.output(ledRojo, GPIO.LOW)
            GPIO.output(ledVerde, GPIO.LOW)
            pulsado = False

        time.sleep(0.1) # si pulsamos rápida/ veremos que algunas se escapan...

