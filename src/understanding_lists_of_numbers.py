"""
las listas tambien pueden almasenar
numeros y de hecho, son ideales para  esto.
python proporciona muchas formas de trabajar
 con listas de numeros.

"""
#metodo built-in range()
"""
el metodo built-in range() genera una serie de numeros,
que se pueden convertir en una lista utilizando

ejemplo:
"""
print("\n")
print("--- Numeros del 0 al 9() ---")
for value in range(10): # genera numeros del 0 al 9
    print(value)
numbers = list(range(10))
print(numbers)  # salida [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("\n")
print("--- Numeros del 1 al 9() ---")
for value in range(1,10): # genera numeros del 1 al 9
    print(value)
numbers = list(range(1,10))
print(numbers)  # salida [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("\n")
print("--- Numeros inpares del 1 al 9() ---") 
for value in range(1,10,2): # genera numeros inpares del 1 al 9
    print(value)    
    odd_numbers = list(range(1,10,2))
print(odd_numbers)  # salida [1, 3, 5, 7

print("\n")
print(" -- Numeros pares del 0 al 9() ---")
for value in range(0,10,2): # genera numeros pares del 0 al 8
    print(value)
    even_numbers = list(range(0,10,2))
print(even_numbers)  # salida [0, 2, 4, 6, 8]

print("\n")
print("tabla del 9")
for value in range(0,91,9): # genera la tabla del 9
    print(value)    
    table_of_9 = list(range(0,91,9))
print(table_of_9)  # salida [0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90]



#cuadrados de los primeros 10 numeros
print("\n")
print("numeros al cuadrado del 1 al 10")
squares = []
for number in range(1,11):
    square = number ** 2
    squares.append(square)
print(squares)  # salida [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print("\n")
print("otra forma de generar una lista de cuadrados")
## mas metodos built-in para trabajar con listas de numeros
digits = [1,2,3,4,5,6,7,8,9,0]

#metodo min()
print("el numero menor es: " + str(min(digits))) # salida 0

#metodo max()
print("el numero mayor es: " + str(max(digits))) # salida 9

#metodo sum()
print("la suma de todos los numeros es: " + str(sum(digits))) # salida