frase = input("hola dime una frase y te dijo cuanto tardarias en decirlo: ")
palabras_separadas = frase.split(" ")
cantidad_de_palabras = len(palabras_separadas)

print("-------------------------------------------")

if cantidad_de_palabras > 120:
    print("No te pedi un testamento men")
    print("-------------------------------------------")
else: 
    print(f"dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras} segundos en decirlo")
    
    print(f"dalto tardaria {round(cantidad_de_palabras *0.77,2)} segundos en decirlo")


