nombreArchivo = str(input("Ingresa nombre del archivo: "))
archivo = open(nombreArchivo+".txt","w")
archivo.write(str(input("Ingrese texto: ")))
archivo.close()