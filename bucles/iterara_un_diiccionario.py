#recorriendo diccionario para obtener la claves
diccionario = {
    "nombre" : "aaron",
    "apellido" : "aedo",
    "edad" : 14
}

#recorriendo diccionario con items() para obtener la clave y el valor
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(F"la clave es: {key} y el valor es: {value}")