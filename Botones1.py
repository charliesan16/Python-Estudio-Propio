from tkinter import *
ventana =Frame(height=400,width=400)
ventana.pack(padx=10, pady=10)
Titulo= Label(text="Graficas en tiempo real de sensores",font=("Verdana",15)).place(x=30,y=50)
boton1= Button(ventana,font=("Verdana",8), text=("Grafica 1"), width=10,heigh=3).place(x=70,y=100)
boton2= Button(ventana,font=("Verdana",8), text=("Grafica 2"), width=10,heigh=3).place(x=270,y=100)
boton3= Button(ventana,font=("Verdana",8), text=("Grafica 3"), width=10,heigh=3).place(x=70,y=300)
boton4= Button(ventana,font=("Verdana",8), text=("Todas las Graficas"), width=30,heigh=3).place(x=170,y=300)

ventana.mainloop()

