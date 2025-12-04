# 1. PROPOSITO

# Aqui lo q se busca es que el estudiante use colecsiones como listas tuplas
# y diccionarios, para guardar datos y moverlos,,, como buscar meter quitar o ordenar.
# Tambien se pide meter coment, casos y concluciones y ps validar las cosas pa que no falle.


# 2. INSTRUCCIONES

# - Meter 6 problemas en un solo archivo .py
# - Todo separado con coment
# - Todo en ingles (variables y prints)
# - Cada problema con descripcion, entradas, salidas, validaciones y casos
# - Al final concluciones y referencias.



# 3. CONVENCIONES 

# - listas para datos q cambian
# - tuplas pa datos fijos q no se mueven
# - diccionarios pa buscar cosas con claves
# - variables en lower_snake_case
# - constantes en UPPER_SNAKE_CASE
# - mensajes en ingles como "Error: invalid input"



# 4. RESUMEN EJECUTIVO

# Las listas son mutables,, osea q puedes cambiar sus cosas. Las tuplas no cambian,
# son inmutavles y sirven pa datos fijos,,, y los diccionarios usan claves pa hallar
# valores rapido. Aqui el doc trae 6 problemas usando esos tipos, con validaciones,
# casitos de prueba y operaciones como append, remove, sort y get. La idea es ver
# casos normal borde y error pa q el algoritmo no truene.



# PROBLEM 1: Basic list operations

# Description: simple sorter using a list of ints
#
# Inputs:
# - list of integers
#
# Outputs:
# - sorted list
#
# Validations:
# - check all items are int
#
# Test cases:
# 1) normal: [5,2,9]
# 2) border: []
# 3) error: ["a",5]

numbers_list = [5, 2, 9, 1]

if all(isinstance(x, int) for x in numbers_list):
    sorted_list = sorted(numbers_list)
    print("Problem 1 result:", sorted_list)
else:
    print("Error: invalid input")



# PROBLEM 2: Tuple indexing

# Description: access a tuple item safely
#
# Inputs:
# - tuple
# - index
#
# Outputs:
# - element or error

coords_tuple = (10, 20, 30, 40)
index = 2  # example

if 0 <= index < len(coords_tuple):
    print("Problem 2 result:", coords_tuple[index])
else:
    print("Error: invalid index")



# PROBLEM 3: Dictionary lookup

# Description: find grade by name
#
# Inputs:
# - dictionary
# - key
#
# Outputs:
# - value or error

grades_dict = {
    "john": 80,
    "maria": 95,
    "david": 70
}

name = "maria"

if name in grades_dict:
    print("Problem 3 result:", grades_dict[name])
else:
    print("Error: name not found")



# PROBLEM 4: Add/remove items in list

# Description: demonstrate append and remove
#
# Inputs:
# - list of strings
#
# Outputs:
# - modified list

items_list = ["apple", "banana", "orange"]

items_list.append("grape")

if "banana" in items_list:
    items_list.remove("banana")

print("Problem 4 result:", items_list)



# PROBLEM 5: Average of a list
#
# Description: compute average
#
# Inputs:
# - list of floats
#
# Outputs:
# - average or error

values = [3.5, 4.0, 5.5, 2.0]

if len(values) > 0:
    avg = sum(values) / len(values)
    print("Problem 5 result:", round(avg, 2))
else:
    print("Error: empty list")



# PROBLEM 6: Iterate dictionary

# Description: show items of a dict
#
# Inputs:
# - dict
#
# Outputs:
# - key/value pairs

products = {
    "mouse": 150,
    "keyboard": 300,
    "monitor": 2200
}

if len(products) > 0:
    for key, value in products.items():
        print(f"Problem 6 item: {key} -> {value}")
else:
    print("Error: dict empty")



# CONCLUSIONES

# Aqui se vio que las listas sn buenas pa cosas q cambian, las tuplas pa cosas fijas
# y diccionarios pa buscar por palabra clave rapido. Los problemas mostraron como
# validar datos pa que no truene y como usar metodos basicos..



# REFERENCIAS

# - python.org
# - w3schools python
# - geeksforgeeks python lists
# - realpython basic structures
# - stackoverflow examples
