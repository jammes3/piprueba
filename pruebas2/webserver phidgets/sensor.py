import os
archivo = open("/sys/class/thermal/thermal_zone0/temp")
a =(archivo.read())
b= a[0:2]

archivo = open("./archivocreado.html", "w") 
archivo.write(b)   

archivo = open("./archivocreado.html")          #abre el archivo
c = (archivo.read())                           #lee el archivo
print(c)                                        #imprime el archivo