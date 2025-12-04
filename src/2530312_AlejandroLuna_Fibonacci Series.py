# Resumen Ejecutivo:
# La serie Fibonacci es una lista de numeros que van sumando
# los 2 anteriores. Mi programa va leer un numero n y mostrar
# los primeros n terminos de la seria. Antes de calcular se
# valida la entrada para evitar erros. Se usa un ciclo para
# generar todo automatico

# Problem: Fibonacci series generator
# Description:
# Program that reads an integer n and prints the first n terms
# of the Fibonacci series starting at 0 and 1

# Inputs:
# - n (int; number of terms to generate)

# Outputs:
# - "Fibonacci series:" followed by the n terms

# Validations:
# - n must be integer
# - n must be >= 1
# - Optional: n <= 50 (if not → error)

# Test cases:
# 1) Normal: n = 7 → Fibonacci series: 0 1 1 2 3 5 8
# 2) Border: n = 1 → Fibonacci series: 0
# 3) Error: n = -3 → Error: invalid input


user_input = input("Number of terms: ")


if not user_input.isdigit():
    print("Error: invalid input")
else:
    n = int(user_input)

    if n < 1 or n > 50:
        print("Error: invalid input")
    else:
      
        first_term = 0
        second_term = 1

        print("Fibonacci series:", end=" ")

        if n == 1:
            print(first_term)
        else:
            print(first_term, second_term, end=" ")
            
            count = 2
            while count < n:
                next_term = first_term + second_term
                print(next_term, end=" ")
                first_term = second_term
                second_term = next_term
                count += 1

        print()  


## Conclusiones
# Usar un ciclo while facilita mucho generar mas terminos sin
# tener que escribirlos a mano. Tambien aprendemos que casos
# como n = 1 o n = 2 son especiales porque imprimen menos nums.
# Esta misma logica se puede usar en otros progrmas como
# sucesos matematecos o recursividad.


# References
# 1) Python Docs - Loops
# 2) https://www.youtube.com/watch?v=7Sv4NmvdHcw
# 3) Apuntes de la clase sobre ciclos
