"""
    slicing a list
"""
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("lista original:", players)

print ( "slice de lista original", players[0:3]) # salida ['charles', 'martina', 'michael']     
print ("slice de lista original", players[1:4]) # salida ['martina', 'michael', 'florence']     
print ("slice de lista original", players[:4])  # salida ['charles', 'martina', 'michael', 'florence']
print ("slice de lista original", players[2:])  # salida ['michael', 'florence', 'eli'] 
print ("slice de lista original", players[-3:]) # salida ['michael', 'florence', 'eli']
print ("slice de lista original", players[5:2])
print ("slice de lista original", players[-3:-1])

"""
Slacing en un for
"""
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("aqui se presenta los primeros 3 jugadores del equipo")
for players in players [0:3]:
print(players.title())

"""
copiando una lista 
"""
my_foods = ['pizza', 'tacos', 'flautas', 'gorditas']
my_foods_1 = my_foods[:]
my_foods_2 = my_foods.copy()
my_foods_3 = list(my_foods)



