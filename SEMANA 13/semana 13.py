def calcular_temperatura_promedio(ciudades_temperaturas):
    # temperaturas promedio por cada ciudad
    promedio_por_ciudad = {}

    # Iterar sobre cada ciudad
    for ciudad, semanas in ciudades_temperaturas.items():
        total_temperaturas = 0
        dias_totales = 0

        # sumar las temperaturas
        for semana in semanas:
            total_temperaturas += sum(semana)
            dias_totales += len(semana)

        # Calcular el promedio y almacenarlo
        promedio_por_ciudad[ciudad] = total_temperaturas / dias_totales

    return promedio_por_ciudad


# Datos Dde 3 semanas cada semana tiene 7 dias.
ciudades_temperaturas = {
    "SANTO DOMINGO": [
        [27, 30, 20, 18, 25, 27, 23],  # Semana 1
        [30, 35, 22, 40, 25, 17, 19],  # Semana 2
        [37, 21, 20, 20, 18, 19, 23],  # Semana 3
        [29, 30, 32, 33, 32, 30, 29],  # Semana 4
    ],
    "QUEVEDO": [
        [15, 17, 18, 20, 23, 19, 24],  # Semana 1
        [31, 27, 20, 19, 25, 30, 28],  # Semana 2
        [30, 25, 30, 27, 33, 37, 39],  # Semana 3
        [40, 35, 31, 38, 36, 29, 32],  # Semana 4
    ],
    "GUAYAQUIL": [
        [13, 15, 10, 18, 20, 21, 25],  # Semana 1
        [27, 22, 16, 21, 25, 15, 28],  # Semana 2
        [11, 23, 31, 22, 19, 26, 33],  # Semana 3
        [30, 24, 31, 24, 34, 37, 22],  # Semana 4
    ]
}

# Llamada a la función
promedios = calcular_temperatura_promedio(ciudades_temperaturas)
print(promedios)
