c0=int(input("Ingrese el numero de prueba="))
n=0
while c0 != 1:
    if c0%2==0:
        c0=c0/2
    else:
        c0=3*c0+1
    print(c0)
    n=n+1
print("Cantidad de conteo=",n)
