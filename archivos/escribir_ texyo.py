with open("archivos\\texto_de_aaron.txt", "w" ,encoding="UTF-8") as archivo:
    #sobreescribiendo el archivo  el archivo
    #archivo.write(input("sobreescritura: "))
    
    #agregando dos lineas con writhlines
    archivo.write("\n")
    archivo.writelines(["sobreescritura\n", "misericordia\n"])
    archivo.write("\n")
    #agregandootras dos lineas
    archivo.writelines(["sobreescrdggggitura\n", "misersssicordia\n"])