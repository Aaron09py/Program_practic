#metodo: dato.metodo()
cadena1 = "hola, soy, Aaron"
cadena2 = "Bienvenido broder"

#convierte a mayuscula
Mayusc = cadena1.upper()
#convierte a minuscula
Minuscula = cadena1.lower()
#convierte Primera letra en mayuscula
Primer_letra_mayusc = cadena1.capitalize()

#buscamos una cadena en otra cadena, si no hay coicidencia devuelve -1
busqueda_find = cadena1.find("A")
#buscando cadena en otra cadena, si no hay coincidencia lanza una exepción
busqueda_index = cadena1.index("a")

#si es numero devuelve true, si no devuelve false
es_numerico = cadena1.isnumeric()
#si es alfanumerico devolvemos true, sino devolvemos false
es_alfanumerico = cadena1.isalpha()
#contamos coincidencias de una cadena dentro de otra cadena, devuelve la cantidad de coincidencias, y si no hay coincidencia devuelve 0
contar_coincidencia = cadena1.count("la")
#contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1)
#verificamos si una cadena empieza con otra cadena dada, si es asi devuelve true
empieza_con = cadena1.startswith("h")
#verificamos si una cadena termian con otra cadena dada, si es asi devuelve true
termina_con = cadena1.endswith("n")
#remplaza un pedazo de la cadena dad por otra cadena dada, si el valor 1, se encuentra en la cadena original, remplaza el valor 1 de l misma, por el valor 2
cadena_nueva = cadena1.replace(cadena1, cadena2)
#separar cadenas con la cadena que le demos
cadena_separada= cadena1.split(",")


print(cadena_separada[0])