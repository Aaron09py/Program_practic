#creando una funcion que nos devuelva los numers primso
#entre el 0 y eo argumento que pasamos

def es_primo(num):
    for i in range(2, num-1):
        if num % i == 0: return False
    return True



#creando una funcion que nos devuelva los numeros primos
#entre el 0 y el argumento que pasamos
def primos_hasta(num):
    primos = []
    for i in range(2,num):
        resultado = es_primo(i)
        if resultado == True: primos.append(i)
    return primos

resultado = primos_hasta(13)
print(resultado)





