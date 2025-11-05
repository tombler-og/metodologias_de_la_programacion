#lists
"""
las listas nos permiten almasenarr informacon
 en un lugar, la cantidad de informaccion que 
 tengas: sean muchos o pocos elementos

 se recomienda nombrar una bariable tipo lista
 en prural.

 en Python los corrchetes [] definen una lista,
 sus elementos van separados por comas.
 Ejemplo:
"""
bicycles=['trek', 'canondale', 'redline', 'specialed', 'gaint']
print(bicycles)

print(bicycles[0].title())

#los indises comiensan en 0 y terrminan en n-1, dode n es el numero de elementos
print(bicycles[3].title())

#Accediendo al ultmo 
print(bicycles[-1].title()) # ultimo elemento
print(bicycles[-2].title())# penultimo elemento
print(bicycles[-5].title())# primer elemento

# utilizando valores de la lista
message = "Mi primer bisicleta fue una " + bicycles[4].upper() + "."
print(message)

message_f = f"mi primer busucleta fue una " + bicycles[4].title() + "."
print(message_f)

## Agregar elementos a una lista
print("\n")
print("Agregar elementos a una lista")
print(bicycles)

print("metodo de las listas para agregar elementos: list_name.append(element)")
bicycles.append("ducati")
print(bicycles)

"""
el metodo apent agrega un elementoal final de una lista

"""
print("\n ---Agregar elementos a una lista metodo append()---")
motorcycles=['honda', 'yamaha', 'susuki']
print(motorcycles) #salida ['honda', 'yamaha', 'susuki']
motorcycles.append('ducati')
print(motorcycles)#salida ['honda', 'yamaha', 'susuki', 'ducati']

"""

"""

## Eliminar elementos de una lista: remove(), pop(), del, clear()
print("\n--- Eliminar elementos de una lista: remove(), pop(), del, clear() ---")

frutas = ['manzana', 'platano', 'cereza', 'platano', 'dátil']
print("Lista inicial:", frutas)

# remove(valor) elimina la primera aparición del valor; lanza ValueError si no existe
frutas.remove('platano')
print("Después de frutas.remove('platano') -> elimina la primera 'platano':", frutas)

# pop() elimina y devuelve el último elemento por defecto
ultimo = frutas.pop()
print(f"frutas.pop() devolvió: {ultimo}")
print("Lista ahora:", frutas)

# pop(indice) elimina y devuelve el elemento en el índice dado
frutas.append('kiwi')
print("Agregado 'kiwi' para demostrar pop(0):", frutas)
primero = frutas.pop(0)
print(f"frutas.pop(0) devolvió: {primero}")
print("Lista después de pop(0):", frutas)

# del elimina un elemento por índice sin devolverlo
frutas.append('mango')
print("Agregado 'mango' para demostrar del:", frutas)
del frutas[1]
print("Después de del frutas[1]:", frutas)

# clear() vacía la lista
frutas.clear()
print("Después de frutas.clear():", frutas)

# Nota: remove() busca por valor; pop() por índice (o último si no se pasa índice);
# del trabaja por índice; clear() deja la lista vacía.


p