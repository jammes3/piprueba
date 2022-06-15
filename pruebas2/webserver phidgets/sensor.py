import os
archivo = open("/sys/class/thermal/thermal_zone0/temp")
a =(archivo.read())
b= a[0:2]

archivo = open("./archivocreado.txt", "w") 
archivo.write(b)   

archivo = open("./archivocreado.txt")          #abre el archivo
c = (archivo.read())                           #lee el archivo
print(c)                                        #imprime el archivo