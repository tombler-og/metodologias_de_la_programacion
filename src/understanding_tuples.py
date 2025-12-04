#tulpes
"""
las tuplas son listas de elementos que no
cambia de tamaño. Las tuplas son inmutables.

se utilizan los elementos () para definir una tupla.
"""
rectangle_measurements = (200, 5) #largo,ancho
print(rectangle_measurements[0])
print(rectangle_measurements[2])

for measure in rectangle_measurements:
    print(measure)

# regresando a las listas

cars = ['bmw', 'porche', 'masda']
print(cars)
cars[0]= "BMW"
cars[1]= "Porshe"
cars[2]= "Mazda"
print(cars)


rectangle_measurements = (200, 50)
#rectangle_measurements[0]=300 #no sirve
#rectangle_measurements[1]=100 #no sirve
rectangle_measurements = (300, 100)

"""
no podemos modificar una tupla directamente 
pero si podemos hacer es cambiar la assignacion 
a una variable que almacena una tupla
"""