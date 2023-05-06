#promedio de duración
otros_curso_min = 2.5
otros_curso_max = 7
otros_curso_promedio = 4
curso_dalto = 1.5

#duracion de crudo
crudo_promedo = 5
crudo_dalto = 3.5



#diferenvia de duración
diferencia_con_min = 100 - curso_dalto / otros_curso_min * 100
diferencia_con_max = round(100 - curso_dalto / otros_curso_max * 100,2)
diferencia_con_promedio = 100 - curso_dalto / otros_curso_promedio * 100

#diferencia de tiepo vacio
tiempo_vacio_promedio = 100 - otros_curso_promedio * 1000 // crudo_promedo / 10
tiempo_vacio_dalto = 100 - curso_dalto * 1000 // crudo_dalto / 10

print("------------------------------")
#mostrando la difrencia de tiempo entre cursos
print((f"el curso de dalto es un: {diferencia_con_min}% mas rapido"))
print((f"el curso de dalto dura un: {diferencia_con_max}% menos que el mas lento"))
print((f"el curso de dalto dura un: {diferencia_con_promedio}% menos que el mas rapids"))
print("------------------------------")
#mostrando la cantidadd de espacios vacios eliminados
print((f"un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio"))
print((f"un curso dalto elimina un {tiempo_vacio_dalto}% de tiempo vacio"))
print("------------------------------")

print(f"ver 10 horas de este curso equivale a ver {round(otros_curso_promedio / curso_dalto *10,1)}")
print(f"ver 10 horas de otros cursos equivale a ver {round(curso_dalto*100 / otros_curso_promedio /10,1)}")
print("------------------------------")
