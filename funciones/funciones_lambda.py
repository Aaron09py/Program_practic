numeros= [0,1,2,3,4,5,6,7,8,9,10,11,13,15,20]

#creando una funcion en lambda multiplicar por 2

multiplicar_por_dos = lambda x : x *2 #para evitar crear bloues en funciones def, evitarlas

#creando funcion comun que diga si es par o no 
#def es_par(num):
#    if num % 2== 1:
#        return True

#usar filter con una funcion comun




#creando lo mismo pero con lambda



numeros_pares = filter(lambda numeros: numeros % 2 == 0,numeros)

print(list(numeros_pares))