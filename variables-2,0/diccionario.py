#creando diccionario con dict()
diccionario = dict (nombre="aaron",apellido="aedo")

#las listas no pueden ser claves y usamos fozenset para meter conjunto

diccionario = {frozenset(["rancio"]):"jajaj"}

#creando diccionario con formkeys()valro por defecto: none

diccionario = dict.fromkeys(["nombre","apellido"])

#creando diccionario con formkeys() cambiando el valor por defecto a "nose"

diccionario = dict.fromkeys(["nombre","apellido"], "nose")

print(diccionario["nombre"])