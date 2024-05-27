# Ejercicio 03
# Intercambiar el valor de 2 variables

a = input("Ingrese la primera variable: ")
b = input("Ingrese la segunda variable: ")

a, b = b, a

print(f"El nuevo valor de a es: {a}")
print(f"El nuevo valor de b es: {b}")
