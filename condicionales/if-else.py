import bcrypt

#


# Pedir al usuario que ingrese su nombre de usuario y contraseña para almacenar
usuario_almacenado = input("Ingrese su usuario: ")
contraseña_almacenada = input("Ingrese su contraseña: ")

# Hashear la contraseña y almacenarla de forma segura
salt = bcrypt.gensalt()
contraseña_hasheada = bcrypt.hashpw(contraseña_almacenada.encode('utf-8'), salt)

print("Registrando con éxito.\n")

# Pedir al usuario que inicie sesión
print("Iniciar sesión.\n")
usuario_ingresado = input("Ingrese su usuario para iniciar sesión: ")
contraseña_ingresada = input("Ingrese su contraseña para iniciar sesión: ")

# Verificar que el usuario y la contraseña sean correctos
if usuario_almacenado != usuario_ingresado:
    print("Usuario incorrecto, intente de nuevo.")
    
elif not bcrypt.checkpw(contraseña_ingresada.encode('utf-8'), contraseña_hasheada):
    print("Contraseña incorrecta, intente de nuevo.")
    
else:
    print(f"iniciando sesión")
