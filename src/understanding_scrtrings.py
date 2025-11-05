"""
string variables







"""
name = "clase de programacion"
print(name)

# title
print(name.title())
print(name)
"""
un metodo es una acicion que python puede 
realizar en un fracmento dentro de datos o
 sobre una variable.

 El punto . despues de una variable
 seguido del metodo() dice que dice 
 que se tiene que ejecutar el metodo title()
 de una bariable name.

 todos los metodos van seguidos e parentesis porque
 en ocaciones nesesita informacion adicional
 para funcionar, la cual iran dentro de los parentesis.
 en esta ocasion, en metodo .title() no requiere 
 informaccion adicional para funcionar.
"""

print("Metodo upper:" ,name.upper())
print("metodo lower:" ,name.lower())


# concatenacion de STRINGS

first_name = "alejandro"
last_name = "luna"
full_name = first_name + " " + last_name

print(full_name)
print(full_name.title())


# Whitespases
"""
un whitespase se refiere a ciualquier caracter 
que no se imprime, es decir un espacio, trabuladores
y finales de linea. laos whitespase se utilizan communmente
para organisar las salidas de tal manera que sea mas amigable
de leer o ver para los usuarios.

Ejmplos:
-trabulador: \t
-salto de linea: \n

"""
print("Whitespase tabulador")
print("python")
print("\tpython")
print("\t\tpython")

print("whitespese salto de linea")
print("languages: \n\tpython\nC \n\tJavasript")


# Eliminaccion de espacios en blanco

programing_languages = " python "
print(programing_languages)
print(programing_languages.rstrip())
print(programing_languages.lstrip())
print(programing_languages.strip())


# syntax Error con string

message = 'una fortaleza de python es su comunidad'
print(message)

message = 'una fortaleza de "python" es su comunidad'
print(message)

# F-strings
famous_person_1 = "Taylor Swift"
message_1 = f"{famous_person_1} una vez dijo, me voy al oxxo en avion"
print()

print(f"{famous_person_1.upper()} una vez dijo me voy al oxxo en avion")
# Actividad

"""
Elije una persona famosa(quien tu quieras)
Elige una cita famosa de esa persona
iguala ambos strings a una variable

1) realiza ca concatenaccion utilizando en signo de suma
2) realiza ls concatenaccion utilizando fstrings
"""
famous_person ="Jorge Harrison"
famous_message ="Amense, los unos a los ortos"

