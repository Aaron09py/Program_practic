#Lista que se puede modificar
lista = ["Aaron","Aaro.nfitt",True,1.70]
#lista que no se puede modificar (tupla)
tupla = ("Aaron","Aaro.nfitt",True,1.70)

#esto es valido
lista[3] = "maquinola"
 
#esto no
#tupla[3] = "maquinola"


#creando conjunto (set)(no se puede acceder los elementos por su indice, no almacena datos duplicados)

conjunto = {"Aaron","Aaro.nfitt",True,1.70}

#esto no es valido
#conjunto[1] = "pedrin"


conjunto2 = {"Aaron","Aaro.nfitt",True,1.70}


#print(conjunto[3]) -no se puede acceder al elemento

# creando un diccionario(dict) (la estroctura es key : value y separamos con ,(comas))

diccionario = {
    
    'nombre' : "Aaron",
    'instag' : "Aaro.fitt",
    'estan_emocionados' : True,
    'altura' : 1.70,
    'dato_duplicado' : "Aaron"
}

print(f"tu altura es: {diccionario['altura']} metros"),
