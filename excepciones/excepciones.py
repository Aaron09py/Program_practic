#creando funcion de suma numerica
def sumar_dos():
    #iniciando bucle
    while True:
        #pidiendo numero
        a = input(f"EL numero a es: ")
        b = input(f"El numero b es: ")   
        #intentando comvertir a entero
        try:
         resultado = int(a) + int(b)
        #si tira excepcion nos devolvera y tendremos que poner los numeros(valores) denuevo:
        except ValueError as e:
          print("Te pedi un numero, mogolico")
          print(f"ERROR: {e}")
        
        #de no tirar exepcion termina el bucle
        else:
            break
    
    #el finaly se ejecuta siempre
        finally:
            print("Manejo de excepcion finalizado")
    #mostrando el resultad
    return resultado

print(sumar_dos())