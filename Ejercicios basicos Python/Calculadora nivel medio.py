print("Bienvenidos a la calculadora \nPara salir escribe Salir")
print("Las operaciones son suma, multi, div y resta")

n1 = input("Ingrese un numero: ")
n2 = input("Ingrese otro numero: ")

operacion = input("Ingrese operacion: ")

if operacion == "suma":
    print("La suma es: ", n1 + n2)
elif operacion == "resta":
    print("La resta es: ", n1 - n2)
elif operacion == "multi":
    print("La multiplicacion es: ", n1 * n2)
elif operacion == "div":
    print("La division es: ", n1 / n2)
else:
    print("Ingrese una operacion valida")
