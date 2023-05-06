#creando una lista con list()
lista = list([14,98,78,True])
#devuelve la catidad de elementos a la lista
cantidad_de_elementos = len(lista)
#agregando elemtos ala lista
lista.append(87)
#<gregando un elemento ala lista con un indice especifico
lista.insert(2,56,)
#agregan varios elementos a la lista
lista.extend([False,2030])
#eliminando un elemeto de la lista (por su indice)
lista.pop(-3) #-1 para eliminar el ultimo, -2 para eliminar el antepenultimo, y asi sucesivamente
#removeindo un elemento de la lista por su valor
lista.remove(14)
#elimina toda ls lista
#lista.clear()

#ordenando la lista en: False, True, y los numeros acendete( si usamos el parametro revere=True lo ordena en reversa)
lista.sort(reverse=True)
#invirtiendo los elementos de una lista
lista.reverse()
#verificando si un elemento se enceuntra en la lista
elemento_encontrado = lista.index(98)

print(elemento_encontrado)



