#forma no optima de sumar valores
#def suma(lista):
#    numeros_sumados = 0
###   for numero in lista:
#       numeros_sumados = numeros_sumados + numero
#   return numeros_sumados

#resultado = suma([5,6,7,8])

#utilizando el operador * como argumento (*args) #forma optima

def suma (nombre,*numeros): #def nombre_funcion(parametro1, parametro2, ...):
    
    numeros_sumados = 0 # Cuerpo de la función
    
    return f"{nombre}, la suma de tus numero es: {sum(numeros)}" #return resultado


resultado = suma("Aaron",5,6,7,8)
print(resultado) 