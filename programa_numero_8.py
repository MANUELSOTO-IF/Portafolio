evaluar = True
while evaluar:
    nombre = str(input("Ingrese nombre de la mamá de Goku: "))
    if nombre.upper() == "GINE":
        evaluar = False
        print("Felicidades :)")
    else:
        print("Nombre incorrecto :( \nIntentelo de Nuevo \n\n")