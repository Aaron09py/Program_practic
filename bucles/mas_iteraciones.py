frutas = ["banana", "manzana","durazno","granada","pera"]
cadena = "hola dalto"
numeros = (2,3,4,5)
#evitando que se coma una fruta (con continue)
for fruta in frutas:
    if fruta == "granada":
        continue
    print(f"me voy a comer una {fruta}")

#evitar que el bucle siga eecutandose ( el else no se ejecuta tampoco)
for fruta in frutas:
    if fruta == "durazno":
        break
    
    print("bucle terminado")

else:
    print("terminado")
    
#recorrer una cadena de texto
for letra in cadena:
    print(letra)
    

#for en una ola linea de codigo   
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)