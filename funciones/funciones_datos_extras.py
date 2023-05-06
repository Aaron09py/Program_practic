#creando una funcion de tres parametros

def frase(nombre,apellido,adjetivo):
    return f"Hola {nombre} {apellido}, sos muy {adjetivo}"

#utilizando keyword arguments
#frase_resultado = frase(nombre="Aaron",apellido="Aedo",adjetivo="capo")

#creando la misma funcion con un valor opciona y un valor por defecto

def frase(nombre,apellido,adjetivo = "tonto"):#adjetivo definido pero se puede cambiar"tonto"
    
    return f"Hola {nombre} {apellido}, sos muy {adjetivo}"

frase_resultado = frase(nombre="Aaron",apellido="Aedo",adjetivo="capo")#cambie el adjetivo predifinido ("tonto")
print(frase_resultado)