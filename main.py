#Impresion de "Hola"
print("hello")
#Suma de dos constantes
print(2+3)
#Multiplicación y Division de dos numeros cualquier
num1=int(input("Ingrese primer numero: "))
num2=int(input("Ingrese segundo numero: "))
print("Multiplicación: ",num1 * num2)
print("Division: ",num1 / num2)
#Evaluación de numeros
mayor1=int(input("Ingrese primer numero: "))
mayor2=int(input("Ingrese segundo numero: "))
mayor3=int(input("Ingrese tercer numero: "))
if mayor1 == mayor2 and mayor2 == mayor3:
    print("Todos los numeros son iguales")
else:
    if mayor1 > mayor2 and mayor1 > mayor3:
        print("El primer numero es mayor a todos")
    if mayor2 > mayor1 and mayor2 > mayor3:
        print("El segundo numero es mayor a todos")
    if mayor3 > mayor1 and mayor3 > mayor2:
        print("El tercer numero es mayor a todos")
#Bonus
opera1 = int(input("Ingresa un primer numero: "))
opera2 = int(input("Ingresa un segundo numero: "))

num = True
while(num != False):
    print("Suma: ", opera1 + opera2)
    print("Resta: ", opera1-opera2)
    print("Multiplicación: ", opera1*opera2)
    num = bool(input("Ingresa 1 para continuar, ingresa 0 para terminar"))
    if num == True:
        opera1 = int(input("Ingresa un primer numero: "))
        opera2 = int(input("Ingresa un segundo numero: "))