# P3-Interruptions
## Observations
### First method (Asking the input nonstop)
The code below is just a normal while loop, where the button is asked is state every loop iteration.
```python
while True:
    if not GPIO.input(pulsadorGPIO): # la lectura siempre da 1 (HIGH/True) excepto al pulsar,
                                    # y solo en ese instante, que da 0 (LOW/False)
        if not pulsado: # con esta variable evitamos considerar más de una vez una pulsación;
                        # puede que se lea +1 vez el estado del pin antes de cambiar su estado
                        # Este fenómeno se conoce como rebote (o bounce). Algunas funciones
                        # permiten establecer un parámetro denominado "bouncetime"
            print("El boton se ha pulsado")
            pulsado = True
    else:
        pulsado = False

    time.sleep(0.1) # si pulsamos rápida/ veremos que algunas se escapan...
```

#### Our feedback:
When we tested this, the problem we had was that when we pressed to fast only one print() was executed.
### Second method (Using wait_for_edge)
In this implementation, the while loop still remains, but instead of asking nonstop, we wait until the state of the button is the desired state, in this case it would be when we release the button.
```python
while True:
    GPIO.wait_for_edge(pulsadorGPIO, GPIO.RISING) # When 0->1. Falling when 1->0. Both when both.
    print("El boton se ha pulsado")
```
#### Our feedback:
Although it is said in the documentation that because of the lack of bounce time the behavior can be flawed and the signal could be doubled, when testing this code we never found that issue. 
### Third method (Using add_event_detect)
This method uses the add_event_detect function to detect the change in the state of the button. The main difference between this method and the ones mentioned above is that this one utilizes asynchronous behavior instead of the normal synchronous behavior, this is possible thanks to add_event_detect.
```python
def callbackSalir (senial, cuadro): # señal y estado cuando se produjo la interrup.
    GPIO.cleanup () # limpieza de los recursos GPIO antes de salir
    sys.exit(0)

def callbackBotonPulsado (canal):
    print("El boton se ha pulsado")

#..........

GPIO.add_event_detect(pulsadorGPIO, GPIO.FALLING, 
callback=callbackBotonPulsado, bouncetime=500) # expresado en ms.

signal.signal(signal.SIGINT, callbackSalir) # callback para CTRL+C
signal.pause() # esperamos por hilo/callback CTRL+C antes de acabar
```
#### Our feedback:
The issue here was the same one we had in the [first implementation](#first-method-asking-the-input-nonstop). Outside of that, the rest was flawless.
## Excercises
### Excercise 1
This first excercise was pretty simple, because the things that we were asked to change were already implemented in the [first method](#first-method-asking-the-input-nonstop). So we copied that features into our code:
```python
pulsado = False

while True:
    if (GPIO.wait_for_edge(pulsadorGPIO, GPIO.RISING)):
    if not pulsado: # assures that only consider one pulse
        print("El boton se ha pulsado")
        pulsado = True
    else:
    pulsado = False
    
    sleep(0.1) # sleep is used in order to allow the correct use of Ctrl+C 
```
### Excercise 2

#### 1

#### 2

#### 3
