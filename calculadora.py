num1=float(input("Digite el valor del numero 1= "))
num2=float(input("Digite el valor del numero 2= "))
operacion=input("Digite el nombre de la operacion(suma,resta,multipliacion,division)= ")
resultado=0
if operacion=='suma':
   resultado=num1+num2
elif operacion=='resta':
   resultado=num1-num2
elif operacion=='multiplicacion':
   resultado=num1*num2     
elif operacion=='division' and num2!=0:
   resultado=num1/num2
else: 
   if num2==0:
       print("Error no es posible dividir num1 sobre cero")
   else:
       print("Elija una operacion valida")   

print(f"El resultado es= {resultado}")
