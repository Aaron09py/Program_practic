#falto el profe y los pibes vn a armar la clase

#pedir nombre y la edad de los compañeros que vinieron hoy a clases


 #funcion para obtener al asistente y profesor
def obtener_compañeros(cantidad_de_compañeros):
    
    #creando una lista con los compañeros
    compañeros = []
    
    #ejecutanto un for para pedir información de cada compañerp
    for i in range(cantidad_de_compañeros):
        nombre = input("Ingrese el nombre del compañero: ")
        edad = int(input("ingrese la edad de los compañeros: "))
        compañero = (nombre,edad)
        
        #agregando la información a la lsta
        compañeros.append(compañero)
        
     #ordenandolos de menor a mayor   
    compañeros.sort(key=lambda x:x[1])
    
    #compañero[X] DEVUELVE UNA TUPLA CON (NOMBRE Y EDAD) Y DEPUES ACCEDEMOS AL NOMBRE
    #definir al asistente y profesor
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    
    #retornamos una tupla
    return asistente,profesor

#desempaquetamos lo que nos retorna la funcion
asistente,profesor = obtener_compañeros(5)

#ejecutamos
print(f"el profesor es: {profesor} y su asistente es: {asistente}")


    