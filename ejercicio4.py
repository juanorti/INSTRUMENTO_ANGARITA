import os
diccionario={}
def buscar_usuario(id):
    if diccionario.get(id) is None:
        return False
    else:
        return True

def registrar_usuario():
    name=input("Ingrese nombres ")
    lastName=input("Ingrese apellidos ")
    age=input("Ingrese edad ")
    height=input("Ingrese estatura ")
    weight=input("Ingrese el peso ")
    usuario=dict(nombre=name,apellido=lastName,edad=age,estatura=height,peso=weight)
    return usuario

menu="Ingrese\n 1 Ingresar Usuario\n 2 Consulta Usuario "
i="si"
while i =="si":
    opcion=input(menu)
    if opcion == "1":
        documento=input("Ingrese el documento del usuario " )
        if not buscar_usuario(documento):
            diccionario[documento]=registrar_usuario()
            print("<<<REGISTRO EXITOSO>>>")
        else:
            print("<<<USUARIO YA EXISTENTE>>>")
            pass
    if opcion == "2":
        documento=input("Ingrese el documento del usuario ")
        if  buscar_usuario(documento):
            datos=diccionario[documento]
            print("Los datos correspondientes son:\n{0}".format(datos))
        else:
            print("<<<USUARIO  NO EXISTENTE>>>")
            pass

    entrada=True
    while entrada==True:    
        try:    
            i=input("Desea continuar:\nDigite  si  -  no ").lower()
            int(i)
            entrada=True
        except ValueError:
            entrada=False
            




    os.system ("cls")

print(diccionario)