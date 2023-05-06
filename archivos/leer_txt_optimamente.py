#abriendo el archivo con whitee open
with open("archivos\\texto_de_aaron.txt", encoding="UTF-8") as archivo:
    #leemos el archivo
    contenido = archivo.read()
    
    #mostrand el archivo
    print(contenido)
    
#no es necesario cerrarlo  al uasr white open