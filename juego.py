numeroSecreto = 999

print(
"""
+==================================+
| Bienvenido a mi juego, muggle!   |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")
numeroJugador = int(input("Ingrese el numero secreto="))
while numeroJugador != numeroSecreto:
    print ("¡Ja, ja! ¡Estás atrapado en mi ciclo!")
    numeroJugador = int(input("Ingrese el numero secreto="))
if numeroJugador == numeroSecreto:
    print("¡Bien hecho, muggle! Eres libre ahora")
