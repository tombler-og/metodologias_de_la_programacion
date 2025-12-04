age = 0

try:

  age = int(input("Escribe tu edad: ")) 
    
except:
    age = -1
    print("Error, ingresaste un caracter no valido")
   
#<>

    
if age >= 100:
      print("tienes mas de un siglo")
elif age >= 18 and age < 100:
      print("eres menor de edad") 
elif age >= 0 and age < 18:
      print("eres menor de edad") 
else:
      print("tuviste un error")


"""
hacer un programa que pregunte la edad de una persona
y responda lo sigiente:
-si la edad es menor o igual a 4, entonses la entrada es gratuita
-si la persona es menor que 18, pero mayor que 4,
entonses la entrada cuesta 200 pesos
-si la edad es mayor o igual a 18, entonses la entrada cuesta 
400 pesos
"""
if age <= 4 and age >= 0:
    print("la entrada es gratuita")             
elif age > 4 and age < 18:    
  print("la entrada cuesta $200")
elif age >= 18:   
   print("la entrada cuesta $400")

#Multiple if
guisos = ["deshebrada", "asado", "salsa verde", "pozole"]
if "deshebrada" in guisos:
    print("Hay guiso de deshebrada")
else:
      print("No hay guiso de deshebrada")
if "asado" in guisos:
    print("Hay guiso de asado")     
else:
     print("no hay guiso de asado")
if "tamales" in guisos:
    print("Hay guiso de tamales")
else:
      print("No tamales")
if "salsa verde" in guisos:
    print("Hay guiso de salsa verde")
else:
      print("No hay guiso de salsa verde")


#lista vasia
print('\n')

guisos = []
if guisos:
   print("Hay guisos disponibles")
else:
    print("No hay guisos disponibles")


#Utilizando varias listas
print('\n')
guisos_disponibles = ["deshebrada", "asado", "salsa verde", "pozole"]
guisos_a_ordenar = ["deshebrada", "caldo de iguana"]

print("¿que guiso deseas ordenar?")
for guiso in guisos_a_ordenar:
    print(f"deseo ordenar: {guiso}")
    if guiso in guisos_disponibles:
        print(f"si tenemos {guiso}")
    else:
        print("perdona no tenemos ese guiso")
print("\nTu orden esta lista")
