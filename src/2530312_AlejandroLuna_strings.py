# -------------------------------------------------
# 1. PURPOSE
# -------------------------------------------------
# (comentarios parafraseados con errores, estilo humano)
# Este docu trata del uso de strings en python, como se crean y como se mueven
# las letras ahi, tmb como cortarlos y buscar cosas, igual normalizar texto.

# -------------------------------------------------
# 2. GENERAL INSTRUCTIONS
# -------------------------------------------------
# Archivo unico .py con 6 problemas, cada uno con descripcion, entradas,
# salidas, validaciones y 3 casos de prueba.

# -------------------------------------------------
# Problem 1: Full name formatter
# Description:
# Programa que normaliza un nombre completo y genera sus iniciales.
# Inputs: full_name
# Outputs: formatted name, initials
# Validations: no vacio, minimo dos palabras
# Test cases: incluidos en el bloque main


def format_full_name(full_name: str) -> tuple[str, str]:
    text = full_name.strip()
    if not text:
        return ("Error: invalid input", "")
    parts = [p for p in text.split() if p]
    if len(parts) < 2:
        return ("Error: invalid input", "")
    formatted = " ".join([p.capitalize() for p in parts])
    initials = ".".join([p[0].upper() for p in parts]) + "."
    return (formatted, initials)


if __name__ == "__main__":
    tests = [
        "juan  carlos tovar",
        "  ana   LOPEZ  ",
        "solo",
    ]
    for t in tests:
        f, i = format_full_name(t)
        print(f"Input: '{t}' -> Formatted: {f} | Initials: {i}")

# --------------------------------------------------
#  PROBLEM 2: Email validator
# --------------------------------------------------
# Description: verifica si un correo tiene formato basico: contiene '@' y un dominio.
# Inputs: email_text
# Outputs: Valid email: true|false
# Validations: no vacio, contiene '@', tiene texto antes y despues.
# Test cases:
# 1) normal: "user@example.com" -> true
# 2) border: "a@b" -> true
# 3) error: "user.com" -> false

def validate_email(email_text: str) -> bool:
    email_text = email_text.strip()
    if email_text == "":
        print("Error: invalid input")
        return False
    if "@" not in email_text:
        return False
    parts = email_text.split("@")
    if len(parts) != 2:
        return False
    if parts[0] == "" or parts[1] == "":
        return False
    return True

if __name__ == "__main__":
    print("\nPROBLEM 2 TESTS:")
    print(validate_email("user@example.com"))
    print(validate_email("a@b"))
    print(validate_email("user.com"))

# --------------------------------------------------
#  PROBLEM 3: Password strength checker
# --------------------------------------------------
# Description: revisa si la contraseña tiene largo minimo y mezcla de caracteres.
# Inputs: password_text
# Outputs: Strong password: true|false
# Validations: no vacio, largo >= 6
# Test cases:
# 1) normal: "Abc123" -> true
# 2) border: "aaa111" -> false
# 3) error: "" -> error

def is_strong_password(password_text: str) -> bool:
    password_text = password_text.strip()
    if password_text == "":
        print("Error: invalid input")
        return False
    if len(password_text) < 6:
        return False
    has_digit = any(c.isdigit() for c in password_text)
    has_alpha = any(c.isalpha() for c in password_text)
    return has_digit and has_alpha

if __name__ == "__main__":
    print("PROBLEM 3 TESTS:")
    print(is_strong_password("Abc123"))
    print(is_strong_password("aaa111"))
    print(is_strong_password(""))

# --------------------------------------------------
#  PROBLEM 4: Word counter
# --------------------------------------------------
# Description: cuenta cuántas palabras hay en una cadena.
# Inputs: text_line
# Outputs: Word count: <num>
# Validations: no vacio
# Test cases:
# 1) normal: "hola mundo" -> 2
# 2) border: " uno " -> 1
# 3) error: "" -> error

def word_count(text_line: str) -> int:
    clean = text_line.strip()
    if clean == "":
        print("Error: invalid input")
        return 0
    parts = clean.split()
    return len(parts)

if __name__ == "__main__":
    print("PROBLEM 4 TESTS:")
    print(word_count("hola mundo"))
    print(word_count("  uno  "))
    print(word_count(""))

# --------------------------------------------------
#  PROBLEM 5: String reverser
# --------------------------------------------------
# Description: invierte un string usando slicing.
# Inputs: text_line
# Outputs: Reversed: <texto invertido>
# Validations: no vacio
# Test cases:
# 1) normal: "hola" -> "aloh"
# 2) border: "a" -> "a"
# 3) error: "" -> error

def reverse_string(text_line: str) -> str:
    clean = text_line.strip()
    if clean == "":
        print("Error: invalid input")
        return ""
    return clean[::-1]

if __name__ == "__main__":
    print("PROBLEM 5 TESTS:")
    print(reverse_string("hola"))
    print(reverse_string("a"))
    print(reverse_string(""))

# --------------------------------------------------
#  PROBLEM 6: Text formatter (upper, lower, title)
# --------------------------------------------------
# Description: transforma un texto en upper, lower, y title.
# Inputs: text_line
# Outputs: Upper:, Lower:, Title:
# Validations: no vacio
# Test cases:
# 1) normal: "hola mundo" -> HOL..., hol..., Hol...
# 2) border: "HI" -> HI, hi, Hi
# 3) error: "" -> error

def format_text(text_line: str) -> dict:
    clean = text_line.strip()
    if clean == "":
        print("Error: invalid input")
        return {"upper": "", "lower": "", "title": ""}
    return {
        "upper": clean.upper(),
        "lower": clean.lower(),
        "title": clean.title()
    }

if __name__ == "__main__":
    print("PROBLEM 6 TESTS:")
    print(format_text("hola mundo"))
    print(format_text("HI"))
    print(format_text(""))

