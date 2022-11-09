
import RPi.GPIO as GPIO
from time import sleep

pulsadorGPIO = 16

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pulsadorGPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    pulsado = False

    while True:
      if (GPIO.wait_for_edge(pulsadorGPIO, GPIO.RISING)):
        if not pulsado: # assures that only consider one pulse
          print("El boton se ha pulsado")
          pulsado = True
      else:
        pulsado = False
      
      sleep(0.1) # sleep is used in order to allow the correct use of Ctrl+C 
