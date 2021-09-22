bloques = int(input("Ingrese el número de bloques de la piramide:"))
altura=0
while bloques:
    altura=altura+1
    bloques=bloques-altura
    if bloques <= altura:
        break

print("La altura de la pirámide:", altura)
