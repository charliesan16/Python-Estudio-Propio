import serial
import time
import collections
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from tkinter import *
from matplotlib.lines import Line2D
import numpy as np
    
def getSerialData(self,Samples,numData,serialConnection,lines):
    for i in range(numData):
        value = float(serialConnection.readline().strip()) #Leer sensor
        data[i].append(value)                              #Guarda lectura en la ultima posicion
        lines[i].set_data(range(Samples),data[i])          #Dibujar nueva linea
serialPort = 'COM7'                                        #Puerto Serial Arduino
baudRate = 9600                                            #Baudios
try:
    serialConnection = serial.Serial(serialPort,baudRate)  #Instanciar objeto serial
except:
    print('No se conecto al puerto')

Samples = 100                                              #Numero de muestras
sampleTime = 100                                           #Tiempo de muestreo
numData=3
#Limites de los Ejes
xmin=0
xmax=Samples
ymin = [0,0,-50,0]
ymax = [6,6,50,100]
lines = []
data = []
for i in range(numData):
    data.append(collections.deque([0] * Samples, maxlen=Samples))
    lines.append(Line2D([],[], color='blue'))
fig = plt.figure()                                          #Crea una nueeva figura
ax1 = fig.add_subplot(2,2,1,xlim=(xmin,xmax),ylim=(ymin[0],ymax[0]))
ax1.title.set_text('Sensor # 1')
ax1.set_xlabel("Samples")
ax1.set_ylabel("volts")
ax1.add_line(lines[0])

ax2 = fig.add_subplot(2,2,2,xlim=(xmin,xmax),ylim=(ymin[1],ymax[1]))
ax2.title.set_text('Sensor # 2')
ax2.set_xlabel("Samples")
ax2.set_ylabel("volts")
ax2.add_line(lines[1])

ax3 = fig.add_subplot(2,2,3,xlim=(xmin,xmax),ylim=(ymin[2],ymax[2]))
ax3.title.set_text('Sensor # 3')
ax3.set_xlabel("Samples")
ax3.set_ylabel("volts")
ax3.add_line(lines[2])
anim = animation.FuncAnimation(fig,getSerialData, fargs =(Samples,numData,serialConnection,lines),interval=sampleTime)
plt.show()

serialConnection.close()

