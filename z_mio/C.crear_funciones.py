
#creando una funcion simple
#def saludar():
#    print("hola lucas, mi maestro")

#ejecutando la funcion simple    
#saludar()

#crear una funcion que tenga parametros

#def saludar(nombre,sexo):
   # sexo = sexo.lower()
   # if (sexo == "mujer"):
  #      adjetivo = "reiana"   
   # elif (sexo == "hombre"):
   #     adjetivo = "titan"
  #  else:
  #      adjetivo = "amor" 
  #  
  #  print(f"hola {nombre}, mi {adjetivo} ¿como estas?")
  #  
#saludar("Aaron","hombre")
#saludar("camila","mujer")
#saludar("fran","no binario")
#crear funcion que retorne valores

###def crear_contraseña_ramdon(num):
#    chars = "a1b2c3d4"
 ##   num_entero = str(num)
 #   num = int(num_entero[0])
##    c1 = num - 2
#    c2 = num
#    c3 = num - 5
#    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
#    return contraseña
    
#password = crear_contraseña_ramdon(0)
#frase = f"Tu contraseña es: {password}"
#print(frase)



#como crear una funcion:
#Para crear una función en Python, se utiliza la palabra clave def, seguida del nombre de la función y 
#los parámetros que recibe entre paréntesis. La sintaxis básica de una función en Python es la siguiente:

#def nombre_funcion(parametro1, parametro2,):
     #...
   #return resultado

 
#ejemplo
#def sumar(num1, num2):
    #resultado = num1 + num2
    #return resultado

#Para utilizar la función, simplemente se llama al nombre de la función y se le pasan los argumentos que requiere. Por ejemplo:
#resultado = sumar(2, 3)
#print(resultado) # Output: 5



#def saludar():
    
    #nombre = input(f"ingresa tu nombre: ")
    #trabajo = input(f"ingresa tu trabajo: ")
    #mensaje = (f"Hola {nombre} como estas en {trabajo}")
    #print(mensaje)
    #respuesta = input("¿Estás bien o mal en programación? ")
    #if respuesta.lower == ("bien"):
    #    respuesta = ("BIen sigue asi")
    #else:
    #    ("Debes esforzarte para tener más exito")

#saludar()

def sumar():
    resultado = int(num1) + int(num2)
    return resultado

num1 = int(input(f"Porfavor dime el primer numero: "))
num2 = int(input(f"Porfavor dime el segundo numero: "))
letra = input(f"Porfavor dime la primer letra: ")
letra2 = input(f"Porfavor dime la segunda letra: ")

suma = num1 + num2
print(f"el resultado de {num1} + {num2} es: ",suma)

suma2 = letra + letra2
print(f"El resultado de la union de {letra} + {letra2} es: ",suma2 )



sumar()

#------------------------------------------------------------------------------#


def sumar(num1, num2):
    resultado = num1 + num2
    return resultado

num1 = int(input("Por favor, ingrese el primer número: "))
num2 = int(input("Por favor, ingrese el segundo número: "))
letra1 = input("Por favor, ingrese la primera letra: ")
letra2 = input("Por favor, ingrese la segunda letra: ")

suma_numeros = sumar(num1, num2)
print(f"La suma de {num1} + {num2} es: {suma_numeros}")

union_cadenas = letra1 + letra2
print(f"La unión de {letra1} + {letra2} es: {union_cadenas}")



