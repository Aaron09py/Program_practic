#creando una funcion que mientre la serie fimonacci entre 0 y numero dado
def fimonacci(num):
    a,b = 0,1
    fimonacci_lista = [0]
    for i in range(num):
        if a >= num: return fimonacci_lista
        else: 
            fimonacci_lista.append(a)
            a,b = b,a+b
        
    return fimonacci_lista

resultado = fimonacci(20)
print(resultado)