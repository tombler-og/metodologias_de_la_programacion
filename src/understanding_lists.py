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
metodo insert() - agrega un elemento en una posicion especifica
"""
print("\n--- agregar un elemento en una posicion especifica ---")
motorcycles=['honda', 'yamaha', 'susuki']       
print(motorcycles) #salida ['honda', 'yamaha', 'susuki']
motorcycles.insert(0, 'ducati')
print(motorcycles) #salida ['ducati', 'honda', 'yamaha', 'susuki']

"""
eliminar elementos de la lista por indice
.pop()
"""         
print("\n--- eliminar elementos de la lista por indice ---")
motorcycles=['honda', 'yamaha', 'susuki']           
print(motorcycles) #salida ['honda', 'yamaha', 'susuki']
popped_motorcycle = motorcycles.pop()
print(motorcycles) #salida ['honda', 'yamaha']              
print("La ultima motocicleta que yo tenia era una " + popped_motorcycle.title() + ".")          


"""
metodo remove() - elimina un elemento por valor
"""
print("\n--- eliminar un elemento por valor ---")   
motorcycles=['honda', 'yamaha', 'susuki', 'ducati']
print(motorcycles) #salida ['honda', 'yamaha', 'susuki', 'ducati']
motorcycles.remove('ducati')
print(motorcycles) #salida ['honda', 'yamaha', 'susuki']
print("\n")



"""
metodo sort() - ordena la lista de manera ascendente
"""
print("\n--- organizar listas de manera permanente ---")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Lista original de carros:", cars)
cars.sort()
print("Lista ordenada de carros (sort()):", cars)
cars.sort(reverse=True)
print("Lista ordenada de carros en orden descendente (sort(reverse=True)):", cars)


"""
ejemplos:

"""
print("\n--- ejemplos de listas ---")
students = ['josue', 'victor', 'ana', 'mike', 'puvlo', 'gerardo']
print(students)
desired_student = input("¿que estudiante deseas eliminar? ")
students.remove(desired_student.strip().lower())
print(students)
print("tu has eliminado a " + desired_student.title() + " de la lista de estudiantes.")
students.reverse()
print(students)

print(len(students))



"""
metodo len() - devuelve el numero de elementos en una lista
metodo reverse() - invierte el orden de los elementos en la lista

"""
print("\n--- ejemplos del metodo sorted() ---")
cars = ['bmw', 'audi', 'toyota', 'subaru', 'ford', 'chevrolet']
print("Lista original de carros:", cars)
cars.reverse()      
sorted_list = sorted(cars)
print("Lista original de carros:", cars)