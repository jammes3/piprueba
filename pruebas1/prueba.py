from gpiozero import Button, LED
import time

boton = Button(17)
rojo = LED(4)
verde = LED(22)

def funcion1():
        print("funcion iniciada")


x = int(input("ingrese un numero: "))

for i in range(x):
        verde.on()
        time.sleep(1)
        verde.off()
        time.sleep(1)


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
