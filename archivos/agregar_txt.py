with open("archivos\\texto_de_aaron.txt", "a" ,encoding="UTF-8") as archivo:
    #usando bucle for para agregar muchas lineas
    for i in range(10): archivo.write("\n"),archivo.write(f"Linea{i+1} agregada\n")  