#empty dictionary fornait
homer_0 = {
    "color": "yellow",
      "bag": "maggie-bag",
        "hair": "two-buns", 
        "dress": "pink",
          "mom":False
          }

print(homer_0)        # {}
print(type(homer_0))  # <class 'dict'>

marge = {
    "color": "yellow",
      "bag": "homer-dounut",
        "hair": "blue",
          "dress": "green",
            "mom": True
            }


gun_0 = {"scar": "yellow", "headshot": 1.5}

##add elements to dictionary
print("\n--- add elements to dictionary ---")

homer_0["x-position"]=15
homer_0["y-position"]=25
homer_0["health"]=100
print(homer_0)

marge["x-position"]=10
marge["y-position"]=30  
marge["health"]=100
print(marge)





covenant_grunt = {
    "color" : "orage",
    "weapon" : "plasma-rifle",
   "armament" : "plasma-grenade" ,
   "health" : 2
}

covenant_elite = {
    "color" : "blue",
    "weapon" : "plasma-rifle",
   "armament" : "plasma-grenade" ,
   "health" : 7
}
covenant_jackal = {
    "color" : "gray",
    "weapon" : "plasma-rifle",
   "armament" : "plasma-grenade" ,
   "health" : 5
}

#list of dictionaries
covenants =[covenant_grunt,
             covenant_elite, 
             covenant_jackal
             ]

for covenant in covenants:
  print("\n", covenant)
  for key, value in covenant.items():
    print(f"{key}: {value}")  

#lista de diccionarios
estudiantes = {
    "santiago": ["reprobado", "prepa_1", "rebelde"],
    "jorge_crack": ["aprobado", "prepa_3", "lider"]
}


#diccionarios en diccionarios

sensors = {
    "temperature": {
      "id" : "temp_01",
      "location" : "lab_1",
      "value" : 23.5,
      "unit" : "C"
    },
    "humedad": {
      "id" : "hum_01",
      "location" : "lab_1",
      "value" : 60.2,
      "unit" : "%"
    }
}

print("\n", "temperature")
print(sensors["temperature"]["value"])

#estudiar metodo get() de los diccionarios
