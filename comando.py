import os
archivo = open("/sys/class/thermal/thermal_zone0/temp")
a =(archivo.read())
b=int(a[0:2])
print(b)
