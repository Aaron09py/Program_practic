#usando open para abrir un archivo con una codificacion unirversal (UTF-8) a archivos
archivo = open("archivos\\texto_de_aaron.txt",encoding="UTF-8")

#leer archivo completo
#
# archivo = archivo.read()

#leer una sola linea
#linea = archivo.readline()


#leer linea por linea
lineas = archivo.readlines()



#cerrar el archivo
archivo.close()


print(lineas)