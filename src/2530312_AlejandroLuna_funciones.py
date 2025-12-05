# Resumen ejecutivo
# Estos programas sirven pa practicar python, ciclos, funciones
# y validaciones del usuario. Son cosas que pasan mucho en la vida
# real como validar emails, sacar fibonacci, ver si un numero es primo
# y asi cosas que se usan bastante en programacion, comas se me olvidan aveces

# PROBLEMA 1: Validar Email


def validate_email(email_text: str) -> bool:
    email_text = email_text.strip()

    if email_text == "":
        print("Error: invalid input.")
        return False

    if "@" not in email_text:
        print("Error: missing '@' symbol")
        return False

    parts = email_text.split("@")
    if len(parts) != 2:
        print("Error: too many '@'")
        return False

    if parts[0] == "" or parts[1] == "":
        print("Error: missing text before or after '@'")
        return False

    print("Email valid, I guess!")
    return True


# PROBLEMA 2: Serie Fibonacci

def fibonacci(n: int):
    if n < 1:
        print("Error: invalid input")
        return

    a, b = 0, 1
    print("Fibonacci:", a, end="")

    for _ in range(1, n):
        print("", b, end=" ")
        a, b = b, a + b
    print() # salto de linea


# PROBLEMA 3: Suma del 1 al n

def sum_1_to_n(n: int) -> int:
    if n < 1:
        print("Error: number too small")
        return 0
    total = 0
    for i in range(1, n+1):
        total += i
    print("Sum is:", total)
    return total


# PROBLEMA 4: Número Primo

def is_prime(number: int) -> bool:
    if number <= 1:
        print("Not prime bro")
        return False
    for i in range(2, number):
        if number % i == 0:
            print("No prime :(")
            return False
    print("Yes prime :)")
    return True


# PROBLEMA 5: Contar vocales

def count_vowels(text: str):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    print("Vowels:", count)
    return count


# PROBLEMA 6: Celsius a Fahrenheit

def celsius_to_fahrenheit(c: float):
    f = (c * 9/5) + 32
    print("Temperature F:", f)
    return f


# PROBLEMA 7: Area de triangulo

def triangle_area(base: float, height: float):
    if base <= 0 or height <= 0:
        print("Error: invalid data")
        return 0
    area = (base * height) / 2
    print("Area is:", area)
    return area


# MAIN MENU (Para probar todo)

def main():
    print("Menu jajaja escoge opcion")
    print("1) Validate email")
    print("2) Fibonacci")
    print("3) Sum 1 to n")
    print("4) Check prime")
    print("5) Count vowels")
    print("6) Celsius to Fahrenheit")
    print("7) Triangle area")

    option = input("Choose option: ")

    if option == "1":
        email_user = input("Email: ")
        validate_email(email_user)

    elif option == "2":
        n = int(input("Enter n: "))
        fibonacci(n)

    elif option == "3":
        n = int(input("Enter n: "))
        sum_1_to_n(n)

    elif option == "4":
        number = int(input("Number: "))
        is_prime(number)

    elif option == "5":
        txt = input("Text: ")
        count_vowels(txt)

    elif option == "6":
        c = float(input("Celsius: "))
        celsius_to_fahrenheit(c)

    elif option == "7":
        base = float(input("base: "))
        height = float(input("height: "))
        triangle_area(base, height)

    else:
        print("Error, invalid option...")

if __name__ == "__main__":
    main()


# Conclusiones
# Aprendi que programar tiene muchas cosas como validar errores
# y que los usuarios siempre rompen todo, pero ya con ciclos y
# funciones es mas facil y tambien pues python esta chido jeje

# Referencias
# - mis apuntes todos feos xd
# - un tutorial de internet ya ni me acuerdo
# - cosas que dijo el profe en el salon
