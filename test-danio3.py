class Personaje:
    def __init__(self, vida, puntos_armadura, efectividad_armadura):
        self.vida = vida
        self.puntos_armadura = puntos_armadura
        self.efectividad_armadura = efectividad_armadura / \
            100  # Convertir a decimal para cálculo

    def recibir_danio(self, danio):
        if self.puntos_armadura > 0:
            # Aplicar la efectividad de la armadura al daño recibido
            danio_reducido = danio * (1 - self.efectividad_armadura)
            # Reducir puntos de armadura en función del daño inicial
            # self.puntos_armadura -= danio
            # Asegurar que los puntos de armadura no sean negativos
            self.puntos_armadura = max(0, self.puntos_armadura)
        else:
            # No hay armadura para proteger, todo el daño va a la vida
            danio_reducido = danio

        # Aplicar daño reducido a la vida
        self.vida -= danio_reducido

        # Verificar si la vida llegó a 0
        if self.vida <= 0:
            print("¡Has muerto!")
            self.vida = 0  # Asegurarse de que la vida no sea negativa


# Crear una instancia de un personaje con valores iniciales
mi_personaje = Personaje(vida=100, puntos_armadura=300,
                         efectividad_armadura=55)  # 50% de efectividad

# Recibir daño
danio_recibido = 200
mi_personaje.recibir_danio(danio_recibido)

# Mostrar los nuevos parámetros
print(f"Has recibido {danio_recibido} de daño!")
print("Vida restante:", mi_personaje.vida)
print("Puntos de armadura restantes:", mi_personaje.puntos_armadura)
