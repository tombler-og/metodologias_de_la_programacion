###Funciones
#las funciones son bloques de codigo reutilizables que realizan una tarea especifica.
#cuando queremos realizar la tarea que se a definido en la funcion
# simplemente llamamos a la funcion por su nombre

"""
sintaxis

 def nombre_funcion ():
        bloque de codigo

"""
def create_full_name(first_name, last_name, middle_name=""):  #Argumentps por posicion y por defecto
    full_name = f"{first_name} {middle_name} {last_name}".title()
    return full_name


first_name = input("ingresa tu nombre: ")
middle_name = input("ingresa tu segundo nombre: ")  
last_name = input("ingresa tu apellido: ")

generated_full_name = create_full_name(
    first_name.strip().lower(),
    last_name.strip().lower(),
    middle_name.strip().lower()
)

print(f"tu nombre completo es: {generated_full_name}") #Arumentos llave

# args en funciones
# kwargs en funciones
# manejo de datos (.txt, .csv, .json, excel, word, pdf)
# args via consola (sys.argv)
# cli en python 
#testing -casos de prueba
#imports
#entripoint


   