cars = ['audi', 'bmw', 'chevrolet', 'corvette', 'tesla']

for car in cars:

    if car == 'bmw'  or car == 'tesla' or car == 'corvette': 
        print(car.upper())
    else:
        print(car.title())
        
print("\n--- Uso de operadores condicionales ---")
#condicionales: el condicional es el corason de un if 
# Condicional True
car = 'bmw'
print(car == 'bmw')  # True

# Condicional False
car_2 = 'Audi'
print(car_2 == 'audi')  # False

# convirtiendo de false a true
car_2 = 'Audi'
print(car_2. lower()== 'audi')  # True


# condicional != para verificar si dos valores no son iguales
requested_topping = 'mushrooms' # string
if requested_topping != 'anchovies': # True
    print("Hold the anchovies!")

# condicionales numericos
age = 18 #int
print(age == 18)  # True

answer = 17
if answer != 42:
    print('esa no es la respuesta correcta. Intenta de nuevo!')

age = 19
print(age < 21)  # True
print(age <= 21)  # True    
print(age > 21)  # False
print(age >= 21)  # False   

#Multiples condiciones
