class Personaje:
    def __init__(self, vida, armadura):
        self.vida = vida
        self.armadura = armadura

    def recibir_danio(self, danio):
        # Calcular la reducción de daño según la armadura
        # Aseguramos que la reducción máxima de daño no exceda el 90%
        reduccion_maxima = 0.9
        factor_reduccion = min(self.armadura * 0.9, reduccion_maxima)
        danio_reducido = danio * (1 - factor_reduccion)

        # Aplicar el daño reducido a la vida
        self.vida -= danio_reducido

        # Verificar si la vida llegó a 0 o menos y ajustar mensaje de salida
        if self.vida <= 0:
            print("¡Has muerto!")
            self.vida = 0  # Asegurarse de que la vida no sea negativa


# Crear una instancia de un personaje con valores iniciales
mi_personaje = Personaje(vida=500, armadura=7500)

# Recibir daño
danio_recibido = 800
mi_personaje.recibir_danio(danio_recibido)

# Mostrar los nuevos parámetros
print(f"Has recibido {danio_recibido} de daño!")
print("Vida restante:", mi_personaje.vida)
