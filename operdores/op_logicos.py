#AND
#Devuelve True si A y B son iguales(True) si A Y B Si son distintos aunque uno sea true devolvera False y si ambos son False devolvera False
Resultado = True & True #Devolver True
Resultado2 = False & False #Devolver Falso
Resultado3 = True & False #Devolver Falso
Resultado4= False & False #Devolver Falso

#OR
#Solo tirara false si  ambos son False( A y B), de lo contrario devolvera True
Resultado5 = True | True #Devolver True
Resultado6 = False | True #Devolver True
Resultado7 = True | False #Devolver True
Resultado8 = False | False #Devolver Falso

#NOT
#invierte el valor, si damos valor True no devolvera False, de lo contrario lo contrario
Resultado9 = not True #Devolver Falso
Resultado10 = not True #Devolver True

print(Resultado)