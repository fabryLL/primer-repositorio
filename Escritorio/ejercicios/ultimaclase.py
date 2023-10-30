numero1 = int(input("ingrese el primer numero: "))
numero2 = int(input("ingrese el segundo numero: "))
numero3 = int(input("ingrese el tercer numero: "))

if numero1 < numero2 < numero3 or numero1 > numero2 > numero3 and numero3 != 3:
    print("la condicion es verdadera")
    print(True)
else:
    print("la condicion es falsa")
    print(False)


# if condicion or otra condicion:
# si la primer condicion es falsa, se compara la segunda condicion
# si la segunda condicion es verdadera, se ejecuta el codigo
# si condicion and otra condicion:
# siempre y cuando todas las condiciones sean verdaderas, se va a ejecutar el codigo
