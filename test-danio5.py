Vida = 350
armadura = 0.85  # Esto es 15% de protección
danio = 1500

# Calcular cuánto daño realmente recibe el personaje después de aplicar la protección de la armadura
danio_reducido = danio * (1 - armadura)

# Calcular la vida restante después de recibir el daño
Vida_restante = Vida - danio_reducido

print("Prueba de funcionalidad:")
print(f"Tu vida inicial es de: {Vida} puntos")
print(f"Has recibido: {danio} puntos de daño")
print(f"Tu armadura te ha protegido reduciendo el daño a: {
      danio_reducido} puntos")
print(f"Tu vida restante es de: {Vida_restante} puntos")
