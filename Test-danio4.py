def calcular_danio(vida, armadura, danio_recibido):
    # Por cada punto de armadura, el daño se reduce un 0.65%
    porcentaje_reduccion = armadura * 0.65 / 100
    # Calculamos el daño efectivo
    danio_efectivo = danio_recibido * (1 - porcentaje_reduccion)
    # Aplicamos el daño a la vida
    vida_restante = vida - danio_efectivo

    # Verificamos si la vida es menor o igual a cero
    if vida_restante <= 0:
        print("¡Has muerto!")
        vida_restante = 0  # Aseguramos que la vida no sea negativa

    return vida_restante


# Datos del personaje
vida_inicial = 100
armadura_personaje = 155
danio_a_recibir = 50

# Calculamos la vida restante después del daño
vida_final = calcular_danio(vida_inicial, armadura_personaje, danio_a_recibir)
print(f"Vida inicial: {vida_inicial}, Vida después de recibir {
      danio_a_recibir} de daño: {vida_final}")
