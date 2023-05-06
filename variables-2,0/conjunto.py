#creando un cojunto (con set)
conjunto = set(["dato1"])

#metiendo un conjunto dentro de otro  conjunto
conjunto1 = frozenset(["dato1", "daro2"])
conjunto2 = {conjunto1, "dato 3"}

#mostrando resultado
print(conjunto2)

#teoria de conjunto
conjunto1 = {1,3,5,7} #conjunto o un super conjunto
conjunto2 = {1,3,7} #un conjunto o un sub conjunto

#verificando si es un subconjunto
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1

#verificando si es un superconjunto
resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 >= (conjunto1)

#verificar si hay un numero en comun o algun (si un numero es igual es false)
resultado = conjunto2.isdisjoint(conjunto1)

print(resultado)