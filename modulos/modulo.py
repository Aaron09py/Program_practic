import modulo_saludar as m_s
import modulo_despedirse as m_p
import modulo_operaciones as op


opcion = input("¿Qué acción quieres realizar? (saludar/a/despedirse/b/): ")

if opcion == "saludar":
    nombre = input("Ingresa tu nombre: ")
    saludo = m_s.saludar(nombre)
    print(saludo)

elif opcion == "a":
    nombre = input("Ingresa tu nombre: ")
    saludo = m_s.saludar(nombre)
    print(saludo)
    

    
    
elif opcion == "despedirse":
    despedida = m_p.despedirse("Aaron")
    print(despedida)  

elif opcion == "a":
    nombre = input("Ingresa tu nombre: ")
    saludo = m_s.saludar(nombre)
    print(saludo) 

else:
    print("Opción no válida.")

opcion = input("¿Qué acción quieres realizar? (sumar/restar/multiplicar/dividir/nada): ")

a = int(input("a es igual a: "))

b = int(input("b es igual a: "))



if opcion == "sumar":
   suma = op.sumar(a, b)
   print(f"el resultado es igual a: {suma}")

elif opcion == "restar":     
   resta = op.restar(a, b)
   print(resta)  

elif opcion == "multiplicar":   
    multiplicación = op.multiplicar(a,b)
    print(multiplicación)

elif opcion == "dividir":
    división = op.dividir(a, b)
    print(división)

elif opcion == "nada":
    print(f"Entendido")