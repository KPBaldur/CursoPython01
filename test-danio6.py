import math


def damage_reduction(armor, k):
    return 1 - math.exp(-k * armor)


# Simulamos con varios valores de armadura y un k elegido
armors = [0, 25, 50, 80, 115, 155, 205, 210]
k_value = 0.0090

# Calculamos la reducción de daño para cada valor de armadura
reductions = [damage_reduction(armor, k_value) for armor in armors]

# Imprimir los resultados
for armor, reduction in zip(armors, reductions):
    print(f"Armadura: {armor}, Reducción de daño: {reduction:.2%}")
