cadena = str(input("Ingresa un mensaje: "))
longitud = len(cadena)-1
lista = list(cadena)
for i in range(len(cadena)):
    print(lista[longitud], end="")
    longitud -= 1