#while
"""
el bucle while ejecuta un bloque de codigo
 mientras una condicion sea verdadera
 
 la sintaxis basica es:
 while condicion:   
        bloque de codigo

"""
#while infinite

"""
si el usuarion escribe un numero entre 
25 y 50, entonses etara dentoro del  rango
y salirse del while
de otro modo pedirle que ingrese otro numero
"""
while True:
    try:
        number =int(input("Ingrese un numero: "))
        
        if number >= 25 and number <= 50:
            print("El numero esta dentro del rango")
            break  # salir del bucle while      
        else:
            print("El numero no esta dentro del rango, intente de nuevo")

    except ValueError:
        print("Por favor, ingrese un numero valido")    
    except KeyboardInterrupt:
        print("\nSaliendo del programa...")
        break  # salir del bucle while    

  

