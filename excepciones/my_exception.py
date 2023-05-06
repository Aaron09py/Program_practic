#excepcion personalizada
class MiExcepcion(Exception):
    def __init__(self,err):
        print(f"Impresinante, cometiste el siguiente error. {err}")
        
#Lanzando mi propia excepcion        
#MiExcepcion("Que Tarado")        

#Manejandola
try:

    raise MiExcepcion("Que Tarado")


except:
    print("como cometes ese error")
    
