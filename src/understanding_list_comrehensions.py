"""
una list comprehension es una forma concisa de crear listas.
Permite generar una nueva lista aplicando una expresión a cada elemento de una secuencia o iterable,
y opcionalmente filtrando elementos según una condición.

"""
squartes = [value**2 for value in range(0,11)]

# para generar los numeros pares del 0 y al 100
evens_range = [value for value in range(0,101,2)]

evens_if = [value for value in range(0,101) if value % 2 == 0]
print(evens_if)



