# RESUMEN EJECUTIVO:
# En este archivo, se practican los tipos numericos en python: enteros y flotantes
# y tambien se tocan los booleanos. La idea es que el estudiante sepa convertir
# entre tipos, redondear, y usar comparaciones logicas para tomar decisiones.
# Se valida que las entradas sean correctas, que no haya divisiones por cero,
# y se muestran salidas claras en ingles. El doc trae 6 problemas con pruebas,
# entradas, salidas y conclusiones.
#
# PRINCIPIOS Y BUENAS PRACTICAS:
# - usar int para contadores y float para cantidades con decimales,,
# - validar siempre que los valores no sean negativos cuando aplique.
# - evitar dividir entre zero, checar el denominador antes.
# - usar nombres descriptivos en ingles y mensajes amigables.


# Problem 1: Temperature converter and range flag
# Description: convert Celsius to Fahrenheit and Kelvin, and flag high temp
# Inputs: temp_c (float)
# Outputs: Fahrenheit, Kelvin, High temperature: true|false
# Validations: temp_c convertible to float, temp_k >= 0
# Test cases:
# 1) Normal: 25.0 -> F=77.0 K=298.15 High=false
# 2) Border: 30.0 -> High=true
# 3) Error: 'abc' -> Error: invalid input

def problem_1_temp_converter(temp_c_input):
    try:
        temp_c = float(temp_c_input)
    except Exception:
        return "Error: invalid input"
    temp_f = temp_c * 9.0 / 5.0 + 32.0
    temp_k = temp_c + 273.15
    if temp_k < 0.0:
        return "Error: invalid input"
    is_high = temp_c >= 30.0
    return f"Fahrenheit: {round(temp_f,2)}\nKelvin: {round(temp_k,2)}\nHigh temperature: {str(is_high).lower()}"



# Problem 2: Work hours and overtime payment
# Description: compute regular, overtime and total pay, flag overtime
# Inputs: hours_worked (float), hourly_rate (float)
# Outputs: Regular pay, Overtime pay, Total pay, Has overtime true|false
# Validations: hours_worked >=0, hourly_rate >0
# Test cases:
# 1) Normal: 45, 10 -> reg=400 ot=75 total=475 has_overtime=true
# 2) Border: 40, 8 -> ot=0 has_overtime=false
# 3) Error: -5,10 -> Error

def problem_2_overtime(hours_input, rate_input):
    try:
        hours = float(hours_input)
        rate = float(rate_input)
    except Exception:
        return "Error: invalid input"
    if hours < 0.0 or rate <= 0.0:
        return "Error: invalid input"
    regular_hours = min(hours, 40.0)
    overtime_hours = max(0.0, hours - 40.0)
    regular_pay = regular_hours * rate
    overtime_pay = overtime_hours * rate * 1.5
    total_pay = regular_pay + overtime_pay
    has_overtime = hours > 40.0
    return f"Regular pay: {round(regular_pay,2)}\nOvertime pay: {round(overtime_pay,2)}\nTotal pay: {round(total_pay,2)}\nHas overtime: {str(has_overtime).lower()}"



# Problem 3: Discount eligibility with booleans
# Description: decide if discount applies and compute final total
# Inputs: purchase_total (float), is_student_text (YES/NO), is_senior_text (YES/NO)
# Outputs: Discount eligible: true|false, Final total
# Validations: purchase_total>=0; texts must be YES or NO
# Test cases:
# 1) Normal: 1200, YES, NO -> eligible true final 1080.0
# 2) Border: 1000, NO, NO -> eligible true
# 3) Error: -5, YES, NO -> Error

def text_to_bool_yes_no(text):
    if not isinstance(text, str):
        return None
    t = text.strip().upper()
    if t == "YES":
        return True
    if t == "NO":
        return False
    return None


def problem_3_discount(purchase_total_input, is_student_text, is_senior_text):
    try:
        purchase_total = float(purchase_total_input)
    except Exception:
        return "Error: invalid input"
    if purchase_total < 0.0:
        return "Error: invalid input"
    is_student = text_to_bool_yes_no(is_student_text)
    is_senior = text_to_bool_yes_no(is_senior_text)
    if is_student is None or is_senior is None:
        return "Error: invalid input"
    discount_eligible = is_student or is_senior or (purchase_total >= 1000.0)
    final_total = purchase_total * 0.9 if discount_eligible else purchase_total
    return f"Discount eligible: {str(discount_eligible).lower()}\nFinal total: {round(final_total,2)}"


# Problem 4: Basic statistics of three integers
# Description: sum, average, max, min and all_even boolean
# Inputs: n1,n2,n3 (ints)
# Outputs: Sum, Average, Max, Min, All even true|false
# Validations: convertible to int
# Test cases:
# 1) Normal: 2,4,6 -> sum 12 avg 4.0 max6 min2 all_even true
# 2) Border: 1,2,3 -> all_even false
# 3) Error: 'a',2,3 -> Error

def problem_4_stats(n1_input, n2_input, n3_input):
    try:
        n1 = int(n1_input)
        n2 = int(n2_input)
        n3 = int(n3_input)
    except Exception:
        return "Error: invalid input"
    sum_value = n1 + n2 + n3
    average_value = sum_value / 3.0
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)
    return f"Sum: {sum_value}\nAverage: {round(average_value,2)}\nMax: {max_value}\nMin: {min_value}\nAll even: {str(all_even).lower()}"



# Problem 5: Loan eligibility (income and debt ratio)
# Description: compute debt ratio and eligibility
# Inputs: monthly_income (float), monthly_debt (float), credit_score (int)
# Outputs: Debt ratio, Eligible true|false
# Validations: monthly_income>0, monthly_debt>=0, credit_score>=0
# Test cases:
# 1) Normal: 10000, 2000, 700 -> ratio 0.2 eligible true
# 2) Border: 8000, 3200, 650 -> ratio 0.4 eligible true
# 3) Error: 0,100,600 -> Error

def problem_5_loan(monthly_income_input, monthly_debt_input, credit_score_input):
    try:
        monthly_income = float(monthly_income_input)
        monthly_debt = float(monthly_debt_input)
        credit_score = int(credit_score_input)
    except Exception:
        return "Error: invalid input"
    if monthly_income <= 0.0 or monthly_debt < 0.0 or credit_score < 0:
        return "Error: invalid input"
    debt_ratio = monthly_debt / monthly_income
    eligible = (monthly_income >= 8000.0) and (debt_ratio <= 0.4) and (credit_score >= 650)
    return f"Debt ratio: {round(debt_ratio,3)}\nEligible: {str(eligible).lower()}"



# Problem 6: Body Mass Index (BMI) and category flag
# Description: compute BMI and flags for underweight/normal/overweight
# Inputs: weight_kg (float), height_m (float)
# Outputs: BMI rounded, Underweight true|false, Normal true|false, Overweight true|false
# Validations: weight>0, height>0
# Test cases:
# 1) Normal: 70,1.75 -> bmi ~22.86 normal true
# 2) Underweight: 50,1.8 -> underweight true
# 3) Error: 0,1.7 -> Error

def problem_6_bmi(weight_input, height_input):
    try:
        weight = float(weight_input)
        height = float(height_input)
    except Exception:
        return "Error: invalid input"
    if weight <= 0.0 or height <= 0.0:
        return "Error: invalid input"
    bmi = weight / (height * height)
    is_underweight = bmi < 18.5
    is_normal = (bmi >= 18.5) and (bmi < 25.0)
    is_overweight = bmi >= 25.0
    return f"BMI: {round(bmi,2)}\nUnderweight: {str(is_underweight).lower()}\nNormal: {str(is_normal).lower()}\nOverweight: {str(is_overweight).lower()}"



# Bloque de pruebas automaticas
if __name__ == "__main__":
    print("--- Problem 1 Tests ---")
    print(problem_1_temp_converter("25"))
    print(problem_1_temp_converter("30"))
    print(problem_1_temp_converter("abc"))

    print("\n--- Problem 2 Tests ---")
    print(problem_2_overtime("45","10"))
    print(problem_2_overtime("40","8"))
    print(problem_2_overtime("-5","10"))

    print("\n--- Problem 3 Tests ---")
    print(problem_3_discount("1200","YES","NO"))
    print(problem_3_discount("1000","NO","NO"))
    print(problem_3_discount("-5","YES","NO"))

    print("\n--- Problem 4 Tests ---")
    print(problem_4_stats("2","4","6"))
    print(problem_4_stats("1","2","3"))
    print(problem_4_stats("a","2","3"))

    print("\n--- Problem 5 Tests ---")
    print(problem_5_loan("10000","2000","700"))
    print(problem_5_loan("8000","3200","650"))
    print(problem_5_loan("0","100","600"))

    print("\n--- Problem 6 Tests ---")
    print(problem_6_bmi("70","1.75"))
    print(problem_6_bmi("50","1.8"))
    print(problem_6_bmi("0","1.7"))



# CONCLUSIONES:
# - Los tipos int y float se usan juntos para resolver problemas reales.
# - Los booleanos salen de comparaciones y permiten tomar decisiones con if.
# - validar las entradas y evitar divisiones por cero es muy importante.
# - combos de and/or son utiles pa reglas compuestas como prestamos o descuentos.
# - redondear los floats ayuda a mostrar resultados legibles.


# REFERENCIAS (minimo 5):
# 1) Python docs - Numeric and Boolean types
# 2) Real Python - numbers and math
# 3) W3Schools - Python numeric types
# 4) GeeksforGeeks - Python operators
# 5) Programiz - Python data types


# GitHub repo (placeholder):
# https://github.com/yourusername/yourrepo