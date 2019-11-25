def contar_letras(palabra):
    contadorLetras=0
    cantidad=len(palabra)
    for i in range(cantidad):
        if palabra[i] != " ":
            contadorLetras+=1
    return contadorLetras


nombre=input("Ingrese el nombre de la persona")
cantidad=contar_letras(nombre)
print("El nombre ingresado tiene una cantidad de: {0}".format(cantidad))

