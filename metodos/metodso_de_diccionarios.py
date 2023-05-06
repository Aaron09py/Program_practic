diccionario = {
    "nombre" : 'Aaron',
    "apelldio" : 'aedo',
    "edad" : 14
}

#nos devuelve dict_item
claves = diccionario.keys()

#obteniendo un elemento con get() (si no encuentra nada el programa continua)
valor_de_edad = diccionario.get("edad")
print("hola papa, el programa continua")

#eliminando todo del diccionario
#diccionario.clear()

#eliminando un elemento del disccionario
diccionario.pop("subs")

#obtenendo un elemento dict_items iterable

diccionario_iterable = diccionario.items()


print(valor_de_edad)