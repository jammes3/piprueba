import os

archivo = open("./archivocreado.txt", "w")      #crea archivo
archivo.write("este es un texto1")              #esribe el archivo
archivo.close()                                 #cierra el archivo

archivo = open("./archivocreado.txt")          #abre el archivo
a = (archivo.read())                           #lee el archivo
print(a)                                        #imprime el archivo