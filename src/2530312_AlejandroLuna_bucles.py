# RESUMEN EJECUTIVO:
# En este archivo se juntan varios programitas en python q muestran como usar bucles for y while ,
# cada uno sirve para repetir cosas de distinta forma. Los for se usan mas cuando ya sabes cuantas veces
# va a correr el ciclo pero el while se usa mas cuando pues no se sabe y dependes de una condicion q lo detenga.
# Aqui tambien se ven contadores acumuladores,,, y la idea es evitar cicloss infinitos.
# Cada problemita trae su descripcion, entradas salidas validaciones y pruebas. y al final unas concluciones.
#
# PRINCIPIOS Y BUENAS PRACTICAS:
# - El for es util cuando ya traes claro el numero de repeticiones,,
# - El while sirve mas cuando dependes de que algo se cumpla o no se cumpla.
# - hay que iniciar contadores y acumuladores antes de entrar al bucle.
# - actualizar las variables dentro del while sino se queda trabado,,
# - mantener el ciclo facilito y sin tanta cosa.


# Problem 1: Sum of range with for
# Descripcion: Este problema hace una suma desde 1 hasta n y tambien saca la suma
# de los pares nada mas. Todo con un for sencillo,,
#
# Entradas:
# - n (int)
#
# Salidas:
# - "Sum 1..n:" total_sum
# - "Even sum 1..n:" even_sum
#
# Validaciones:
# - n debe ser entero y mayor o igual que 1 sino marca error..
#
# Pruebas:
# 1) Normal: n=10 -> Sum 55 y la suma par 30.
# 2) Borde: n=1 -> sum 1 y pares 0.
# 3) Error: n=0 o texto raro -> Error.

def problem_1_sum_range(n_input):
    try:
        n = int(n_input)
    except Exception:
        return "Error: invalid input"
    if n < 1:
        return "Error: invalid input"
    total_sum = 0
    even_sum = 0
    for i in range(1, n + 1):
        total_sum += i
        if i % 2 == 0:
            even_sum += i
    return f"Sum 1..n: {total_sum}\nEven sum 1..n: {even_sum}"



# Problem 2: Multiplication table with for
# Descripción: Genera una tabla de multiplicar desde 1 hasta m usando un bucle for.
#
# Entradas:
# - base (int)
# - m (int)
#
# Salidas:
# - Líneas como "5 x 1 = 5"
#
# Validaciones:
# - base y m deben ser enteros; m >= 1
#
# Casos de prueba:
# 1) Normal: base=5, m=4
# 2) Borde: base=3, m=1
# 3) Error: m=0 o m="a" -> Error: invalid input

def problem_2_multiplication_table(base_input, m_input):
    try:
        base = int(base_input)
        m = int(m_input)
    except Exception:
        return "Error: invalid input"
    if m < 1:
        return "Error: invalid input"
    lines = []
    for i in range(1, m + 1):
        lines.append(f"{base} x {i} = {base * i}")
    return "\n".join(lines)



# Problem 3: Average of numbers with sentinel
# Descripción: Lee números flotantes hasta que el usuario ingrese el valor sentinela -1.
# Calcula el promedio y la cantidad de valores ingresados.
#
# Entradas:
# - números repetidos (float)
# - sentinela: -1
#
# Salidas:
# - "Count:" cantidad
# - "Average:" promedio
# - "Error: no data" si no se ingresan datos válidos
#
# Validaciones:
# - Cada entrada debe ser convertible a float
#
# Casos de prueba:
# 1) Normal: [10,20,30,-1]
# 2) Borde: [-1]
# 3) Error: ["a",5,-1] -> Error: invalid input

def problem_3_average_with_sentinel(inputs):
    SENTINEL_VALUE = -1.0
    total = 0.0
    count = 0
    for token in inputs:
        try:
            value = float(token)
        except Exception:
            return "Error: invalid input"
        if value == SENTINEL_VALUE:
            break
        total += value
        count += 1
    if count == 0:
        return "Error: no data"
    return f"Count: {count}\nAverage: {total / count}"



# Problem 4: Count positives with while (attempts)
# Descripción: El usuario ingresa números hasta alcanzar un máximo de intentos.
# Se cuentan solo los positivos.
#
# Entradas:
# - lista de entradas
# - MAX_ATTEMPTS
#
# Salidas:
# - "Positive count:" número de positivos
#
# Validaciones:
# - Cada entrada debe convertirse a float
#
# Casos de prueba:
# 1) Normal: [1,2,-3], max=3
# 2) Borde: [0], max=1
# 3) Error: ["xx",2], max=3

def problem_4_count_positives(inputs, max_attempts):
    count = 0
    attempts = 0
    for token in inputs:
        if attempts >= max_attempts:
            break
        attempts += 1
        try:
            value = float(token)
        except Exception:
            return "Error: invalid input"
        if value > 0:
            count += 1
    return f"Positive count: {count}"


# Problem 5: Menu with while
# Descripción: Simula un menú interactivo: sumar valores, reiniciar total o salir.
#
# Entradas:
# - lista de opciones en texto
#
# Salidas:
# - cadenas indicando acciones
#
# Validaciones:
# - opciones válidas: add, reset, exit, other -> error
#
# Casos de prueba:
# 1) Normal: ["add","add","exit"]
# 2) Borde: ["exit"]
# 3) Error: ["invalid"]

def problem_5_menu_simulator(options):
    total = 0
    log = []
    for op in options:
        op_clean = op.strip().lower()
        if op_clean == "add":
            total += 1
            log.append(f"Total: {total}")
        elif op_clean == "reset":
            total = 0
            log.append("Total: 0")
        elif op_clean == "exit":
            log.append("Exiting menu")
            break
        else:
            return "Error: invalid input"
    return "\n".join(log)



# Problem 6: For over list
# Descripción: Recorre una lista usando for y calcula suma, mínimo y máximo.
#
# Entradas:
# - lista de números
#
# Salidas:
# - sum, min, max
#
# Validaciones:
# - todos los elementos deben ser numéricos
#
# Casos de prueba:
# 1) Normal: [1,2,3,4]
# 2) Borde: [5]
# 3) Error: [1,"x",3]

def problem_6_list_stats(values):
    parsed = []
    for token in values:
        try:
            parsed.append(float(token))
        except Exception:
            return "Error: invalid input"
    return f"Sum: {sum(parsed)}\nMin: {min(parsed)}\nMax: {max(parsed)}"



# Bloque de pruebas automaticas
if __name__ == "__main__":
    print("--- Problem 1 Tests ---")
    print(problem_1_sum_range("10"))  # Normal
    print(problem_1_sum_range("1"))   # Borde
    print(problem_1_sum_range("0"))   # Error

    print("\n--- Problem 2 Tests ---")
    print(problem_2_multiplication_table("5", "4"))  # Normal
    print(problem_2_multiplication_table("3", "1"))  # Borde
    print(problem_2_multiplication_table("2", "0"))  # Error

    print("\n--- Problem 3 Tests ---")
    print(problem_3_average_with_sentinel(["10", "20", "30", "-1"]))  # Normal
    print(problem_3_average_with_sentinel(["-1"]))  # Borde
    print(problem_3_average_with_sentinel(["a", "5", "-1"]))  # Error

    print("\n--- Problem 4 Tests ---")
    print(problem_4_count_positives(["1", "2", "-3"], 3))  # Normal
    print(problem_4_count_positives(["0"], 1))  # Borde
    print(problem_4_count_positives(["xx", "2"], 3))  # Error

    print("\n--- Problem 5 Tests ---")
    print(problem_5_menu_simulator(["add", "add", "exit"]))  # Normal
    print(problem_5_menu_simulator(["exit"]))  # Borde
    print(problem_5_menu_simulator(["invalid"]))  # Error

    print("\n--- Problem 6 Tests ---")
    print(problem_6_list_stats(["1", "2", "3", "4"]))  # Normal
    print(problem_6_list_stats(["5"]))  # Borde
    print(problem_6_list_stats(["1", "x", "3"]))  # Error


# Conclusiones
# En este documento se aplicaron bucles for y while en distintos contextos:
# recorridos de rangos, listas, sentinelas, menús y control de intentos.
# Se reforzó la importancia de la validación de entradas y de evitar ciclos
# infinitos mediante condiciones claras.


# Referencias
# 1. Documentación oficial de Python (python.org)
# 2. W3Schools Python Tutorial
# 3. Real Python - Loop Guides
# 4. Programiz - Python Loops
# 5. StackOverflow - Python Q&A


# Github Repository (placeholder):
# https://github.com/username/repo