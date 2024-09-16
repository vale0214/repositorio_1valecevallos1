# Definir la función calcular_descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    # Calcular el descuento
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento

#monto total de la compra
monto1 = 320
descuento1 = calcular_descuento(monto1)

# Llamada a la función con el monto total porcentaje de descuento
monto2 = 820
porcentaje_descuento_especifico = 15
descuento2 = calcular_descuento(monto2, porcentaje_descuento_especifico)

# montos finales
monto_final1 = monto1 - descuento1
monto_final2 = monto2 - descuento2

# resultados
print(f"Monto 1: {monto1}, Descuento: {descuento1}, Monto final: {monto_final1}")
print(f"Monto 2: {monto2}, Descuento: {descuento2}, Monto final: {monto_final2}")
