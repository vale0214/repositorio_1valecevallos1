# Crear un diccionario con mi información personal
informacion_personal = {
    "nombre": "Valentina Cevallos",
    "edad": 32,
    "ciudad": "Santo domingo",
    "profesion": "estudiante"
}

# Acceder y modificar el valor de la clave "ciudad" y agrego parroquia
informacion_personal["ciudad"] = "Santo domingo Bomboli"

# Agregar una nueva clave-valor para la "profesion" que estudia
informacion_personal["profesion"] = "ingenieria de la informacion"

# Verificar existencia de la clave "telefono" agregar en caso de no existir
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "968275982"

# Eliminar la clave "edad" del diccionario
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimir el diccionario final
print(informacion_personal)
