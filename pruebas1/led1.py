from gpiozero import Button, LED
from signal import pause

boton = Button(17)
rojo = LED(4)
verde = LED(22)

def funcion1():
        print("funcion iniciada")
'''
while True:
        if boton.is_pressed:
                verde.on()
                funcion1()
                rojo.off()
                print("led verde encendido")
        else:
                rojo.on()
                verde.off()
                print("led rojo encendido")
'''
'''
def say_hello():
    print("Hello!")

def say_goodbye():
    print("Goodbye!")


boton.when_pressed = say_hello
boton.when_released = say_goodbye

pause()
'''



def say_hello():
    rojo.on()
    verde.off()
    print("Hello!")

def say_goodbye():
    rojo.off()
    verde.on()
    print("Goodbye!")

boton.when_pressed = say_hello
boton.when_released = say_goodbye

pause()
