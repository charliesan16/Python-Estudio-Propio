
beatles=[]
#Paso 1: Crea una lista vacía llamada beatles.
print("Paso 1:", beatles)
# Paso 2: Emplea el método append() para agregar los siguientes miembros de la banda a la lista: John Lennon, Paul McCartney y George Harrison.
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Paso 2:", beatles)

# Paso 3: Emplea el ciclofor y el append() para pedirle al usuario que agregue los siguientes miembros de la banda a la lista: Stu Sutcliffe, y Pete Best.
for i in range(2):
    nombre=input("Ingrese el nombre=")
    beatles.append(nombre)
print("Paso 3:", beatles)

# Paso 4: Usa la instrucción del para eliminar a Stu Sutcliffe y Pete Best de la lista.

del (beatles[4])
del (beatles[3])
print("Paso 4:", beatles)

# Paso 5: Usa el método insert() para agregar a Ringo Starr al principio de la lista.
beatles.insert(0,"Ringo Starr")
print("Paso 5:", beatles)


# probando la longitud de la lista
print("Los Fab", len(beatles))
