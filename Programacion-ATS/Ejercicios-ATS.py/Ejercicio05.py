# Ejercicio 05
# Calcular el descuento del 15% para el total de una compra

compra = float(input("Ingresa el producto: "))

descuento = compra * 0.15
precio_final = compra - descuento

print(f"El precio final a pagar es de ${precio_final:.1f}")
