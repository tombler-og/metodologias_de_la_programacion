"""
vamos a realzar un  programa que defina un PIN
para dar axeso a un usuario

el usuario tendra 3 intentos para ingresar el PIN correcto

si el usuario sibrepasa el intento maxiomo de ingtentos
se va a bloquear el acceso


"""
CORRECT_PIN = "1234"
MAX_ATTEMPTS = 5
attempts = 0

while attempts < MAX_ATTEMPTS:
    user_input = input("ingresa tu PIN: ")
    
    if user_input == CORRECT_PIN:
        print("Acceso concedido :) you not idiot :)")
        break
    else:
        attempts += 1
        reamaining_attempts = MAX_ATTEMPTS - attempts
       
        print("PIN incorrecto. Te quedan " + str(reamaining_attempts) + " intentos.")
else:
         print("\n","Acceso bloqueado :) you are idiot :)")    
