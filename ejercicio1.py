def comparar_numeros(a,b):
    if a>b:
        return a
    if b>a:  
        return b
    if a == b:
        return False

num1=float(input("Ingrese numero1"))
num2=float(input("Ingrese numero2"))

mayor=comparar_numeros(num1,num2)

if not mayor:
    print("Los numeros ingresados son iguales") 
else:
    print("El numero mayor ingresado por el usuario es:{0}".format(mayor))