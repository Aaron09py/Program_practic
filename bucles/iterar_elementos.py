animales = ["gato","perro","loro","cocodrilo"]
numeros = ((11,12,13,14))

#recorriendo ls lista e animales
for animal in animales:
    print(f"Ahora la variable nimal es igual a:  {animal}")
  
#recorriendo la lista numero y multiplicando cada valor por 2  
for numero in numeros:
    resultado = numero * 2
    print(resultado)

#iterando dos lstas del mismo tamaño al mismo tiempo  
for numero,animal in zip(animales,numeros):
    print(f"recorriendo lista 1:  {numero}")
    print(f"recorriendo lista 2: {animal}")
    
#forma no optima de recorres una lista 
for num in range(len(numeros)):
    print(numeros[num])
    
#forma correcta
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]

    print(f"el indice es: {indice} y el valor es: {valor}")

#usando for con else
for numero in numeros:
    print(f"ejecutando en ultimo bucle, valor actual: {numero}")
else:
    print("el nucle termino")

#todo lo anterios es igual para listas y tuplas 









