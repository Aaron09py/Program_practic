import re

texto = """Hola loquito. esta es la cadena 1. como estas mi capitan.
Esta es la inea 2 de texto.
Esta es la inea 2456 de texto. abab abab abab abab abab
y Esta es la ultima (linea 3) difinitiva mi capitan"""
#haciendo una busqueda simple
#resultado = re.findall("Esta",texto)

#\d -> busca digitos numericos de 0 al 9
#resultado = re.findall(r"\d",texto)

#\D ->busca TODO MENOS digitos numericos del 0 al 9
#resultado = re.findall(r"\D",texto)

#\w -> busca caracteres alfanumericos [a-z A-Z 0-9 _]
#resultado = re.findall(r"\w",texto)

#\W -> busca TODO MENOS caracteres alfanumericos [a-z A-Z 0-9 _]
#resultado = re.findall(r"\W",texto)

#\s -> busca espacios en blanco [espacios, tabs, saltos de lineas]
#resultado = re.findall(r"\s",texto)

#\D -> busca TODO MENOS espacios en blanco [espacios, tabs, saltos de lineas]
#resultado = re.findall(r"\S",texto)

#. -> busca TODO MEOS saltos en linea
#resultado = re.findall(r".",texto)

#\n -> busca saltos en linea
#resultado = re.findall(r"\n",texto)

#\ cancelmos caracteres especiales, cancelando funcion de [.] y buscado puntos
#resultado = re.findall(r"\.",texto)

#armando una cadena que busque un numero, seguido de un punto y un esspacio

#resultado = re.findall(r"\d\.",texto)

#^ -> buscando Hola al principio de una linea
#resultado = re.findall(r"^Esta",texto,flags=re.M)

#^ -> buscando capitan al final de una linea
#resultado = re.findall(r"capitan$",texto)

#{n} -> busca n cantidad de vecez el alor de la izquierda
#resultado = re.findall(r"\d{3}\s",texto)

#{n,m} -> busca n cantidad como un minimo y m como un maximo
#resultado = re.findall(r"(ab){1,4}",texto)

#{n} -> busca n cantidad por x
#resultado = re.findall(r"(ab){2}",texto)

#| -> busca una cosa o la otra
resultado = re.findall(r"\d{2,4}\s|Hola",texto)

print(resultado)