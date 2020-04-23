#Funcion para dibujar un triangulo.
def triangulo():
    inicio = int(input("Ingrese la altura del triangulo: "))
    temp = 1
    temp2 = inicio
    for i in range(inicio):
        for i in range(temp2):
            print("*", end="")
        print("")
        for i in range(temp):
            print(" ", end="")
        temp += 1
        temp2 -= 1
#Funcion para dibujar un cuadrado
def cuadro():
    inicio = int(input("Ingrese lado del cuadro: "))
    temp1 = inicio
    temp2 = inicio
    for i in range(inicio):
        temp3 = temp1
        for i in range(temp1):
            if temp2 == inicio or temp2 == 1:
                print("*", end="")
            else:
                if temp3 == inicio or temp3 == 1:
                    print("*", end="")
                else:
                    print(" ", end="")
                temp3 -= 1
        temp2 -= 1                
        print("")

cuadro()