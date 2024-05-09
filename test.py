class Personaje:
    def __init__(self, vida, energia, armadura, escudo):
        self.vida = vida
        self.energia = energia
        self.armadura = armadura
        self.escudo = escudo

    def recibir_danio(self, danio):
        # Reducir el daño según la armadura
        danio_reducido = danio * (1 - (self.armadura * 0.0065))
        
        # Si hay escudo, reducir el daño del escudo primero
        if self.escudo > 0:
            danio_restante_escudo = max(0, danio_reducido - (self.escudo * 1.75))
            self.escudo = max(0, self.escudo - (danio / 1.75))
            danio_reducido = danio_restante_escudo

        # Si el escudo no es suficiente para cubrir todo el daño, reducir la vida
        self.vida = max(0, self.vida - danio_reducido)

        # Verificar si la vida llegó a 0
        if self.vida == 0:
            print("¡Has muerto!")

# Crear una instancia de un personaje con valores iniciales
mi_personaje = Personaje(vida=100, energia=80, armadura=50, escudo=20)

# Recibir daño
danio_recibido = 10
mi_personaje.recibir_danio(danio_recibido)

# Mostrar los nuevos parámetros
print("Vida restante:", mi_personaje.vida)
print("Energía:", mi_personaje.energia)
print("Armadura:", mi_personaje.armadura)
print("Escudo restante:", mi_personaje.escudo)
