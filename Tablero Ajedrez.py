EMPTY = "-"
TORRE = "TORRE"
A="Arfil"
tablero = []

for i in range(8):
    fila = [EMPTY for i in range(8)]
    tablero.append (fila)

tablero[0][0] = TORRE
tablero[0][1] = A
tablero[0][6] = A
tablero[0][7] = TORRE
tablero[7][0] = TORRE
tablero[7][7] = TORRE

print(tablero)
