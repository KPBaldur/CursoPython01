class Personaje:
    def __init__(self, vida, energia, armadura, escudo):
        self.vida = vida
        self.energia = energia
        self.armadura = armadura
        self.escudo = escudo

    def recibir_danio(self, danio):
        # Calculamos el daño recibido por el escudo primero
        if self.escudo > 0:
            danio_escudo = danio * 1.25  # El escudo recibe 1.25 veces el daño
            if danio_escudo <= self.escudo:
                self.escudo -= danio_escudo
                danio = 0  # Todo el daño es absorbido por el escudo
            else:
                # Calcular el daño restante después del escudo
                danio = (danio_escudo - self.escudo) / 1.25
                self.escudo = 0

        # Reducimos el daño restante segun la armadura
        if danio > 0:
            factor_reduccion = (self.armadura * 0.0065)
            danio_reducido = danio * (1 - factor_reduccion)
            self.vida -= danio_reducido

        if self.vida <= 0:
            print("¡Has muerto!")
            self.vida = 0  # aqui evitamos que la vida no pase a negativo


# Crearmos un personaje con sus estadisticas
mi_personaje = Personaje(vida=100, energia=80, armadura=160, escudo=20)

# Recibir daño
danio_recibido = 1500
mi_personaje.recibir_danio(danio_recibido)

# Mostrar los nuevos parámetros
print(f"Has recibido {danio_recibido} de daño!")
print("Vida restante:", mi_personaje.vida)
print("Energía:", mi_personaje.energia)
print("Armadura:", mi_personaje.armadura)
print("Escudo restante:", mi_personaje.escudo)
