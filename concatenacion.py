palabraSinVocal = ""
userWord= input("Ingrese la palabra=")
userWord= userWord.upper()

for letra in userWord:
    if letra =="A":
        continue
    elif letra == "E":
        continue
    elif letra == "I":
        continue
    elif letra == "O":
        continue
    elif letra == "U":
        continue
    palabraSinVocal=palabraSinVocal +  letra # operacion de concatenación
print(palabraSinVocal)   
