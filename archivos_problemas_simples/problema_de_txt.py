Nombres = ["aaron","lucas","matias","antonilo","militao"]
Apellidos = ["aedo","flores","quezada","milino","ernestiño"]

with open("archivos_problemas_simples\\nombres_y_listas.txt", "w") as archivo:
    archivo.writelines("los datos son: \n\n")
    [archivo.writelines(f"nombre: {n}\nApellido: {a}\n-------\n") for n,a in zip(Nombres,Apellidos)] 