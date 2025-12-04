
# RESUMEN EJECUTIVO

# En este trabajo se hizo un programa CRUD,
# en Python que sirve para manejar articulos en memoria.
# CRUD significa Crear, Leer Actualizar y tambien borrar.
# Se uso un diccionario por que hace mas fácil encontrar los datos
# y las funciones ayudan a organizar el codig, asi no se hace bolas
# el menú deja que el usuario aga las operaciones mas rpido


# PROBLEMA DEL CRUD

# Este programa controla un inventario muy simple,
# los artículos tienen: un id un nombre, un precio
# y una cantidad disponible, todo se guarda en un diccionario
# donde la llave es el id de cada articulo.

# Entradas:
# opciones del menu,, id nombre precio cantidad

# Salidas:
# mensajes del sistemaa como:
# "Artículo creado" , "Artículo no encontrado" , etc.

# Validaciones:
# no permite campos vacios ni datos que no sean números
# y no se deja crear un id que ya exista en la lista

# Casos de prueba
# 1 normal: crear, leer, actualizar,, eliminar un articulo normal
# 2 borde: cantidad en 0 si deja hacerlo
# 3 error: intentar leer o borrar algo que no existe

# Se eligio un diccionario por que asi se busca rapidísimo
# sin recorrer toda la lista y ayuda a evitar duplicados.

# FUNCIONES CRUD

def create_item(items, item_id, name, price, quantity):
    if item_id in items:
        print("Error, el artículo ya existe")
        return False
    items[item_id] = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    print("Artículo creado bien")
    return True


def read_item(items, item_id):
    if item_id not in items:
        print("Artículo no encontrado :( ")
        return None
    item = items[item_id]
    print(f"ID: {item_id} | Nombre: {item['name']} | Precio: {item['price']} | Cantidad: {item['quantity']}")
    return item


def update_item(items, item_id, name, price, quantity):
    if item_id not in items:
        print("Artículo no encontrado")
        return False
    items[item_id] = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    print("Artículo actualizado ok")
    return True


def delete_item(items, item_id):
    if item_id not in items:
        print("Artículo no encontrado!!!")
        return False
    del items[item_id]
    print("Artículo eliminado,")
    return True


def list_items(items):
    if not items:
        print("No hay articulos en la lista")
        return
    print("Listado de articulos guardados:")
    for item_id, item in items.items():
        print(f"{item_id}: {item['name']} - ${item['price']} - Cantidad {item['quantity']}")


# VALIDACIONES Y COSAS EXTRA

def input_number(prompt, allow_float=False):
    value = input(prompt).strip()
    try:
        return float(value) if allow_float else int(value)
    except:
        print("Error: dato invalido")
        return None


def validate_non_empty(field_value):
    return bool(field_value and field_value.strip())


# MENÚ PRINCIPAL DEL PROGRAMA

def main():
    items = {}

    while True:
        print("\n--- MENU DEL CRUD ---")
        print("1 Crear artículo")
        print("2 Leer artículo")
        print("3 Actualizar artículo")
        print("4 Eliminar artículo")
        print("5 Listar todos los artículos")
        print("0 Salir")

        option = input("Elige una opccion: ").strip()

        if option == "0":
            print("Saliendo. bye")
            break

        elif option == "1":
            item_id = input("ID del artículo: ").strip()
            if not validate_non_empty(item_id):
                print("Error: dato vacio")
                continue
            name = input("Nombre del artículo: ").strip()
            if not validate_non_empty(name):
                print("Error: dato vacio")
                continue
            price = input_number("Precio: ", allow_float=True)
            if price is None or price < 0:
                print("Error: precio malo")
                continue
            quantity = input_number("Cantidad: ")
            if quantity is None or quantity < 0:
                print("Error: cantidad mala")
                continue
            create_item(items, item_id, name, price, quantity)

        elif option == "2":
            item_id = input("ID del artículo: ").strip()
            if not validate_non_empty(item_id):
                print("Error: entrada invalida")
                continue
            read_item(items, item_id)

        elif option == "3":
            item_id = input("ID del artículo: ").strip()
            if not validate_non_empty(item_id):
                print("Error: dato vacio")
                continue
            name = input("Nuevo nombre: ").strip()
            if not validate_non_empty(name):
                print("Error de nombre")
                continue
            price = input_number("Nuevo precio: ", allow_float=True)
            if price is None or price < 0:
                print("Error en precio")
                continue
            quantity = input_number("Nueva cantidad: ")
            if quantity is None or quantity < 0:
                print("Error cantidad")
                continue
            update_item(items, item_id, name, price, quantity)

        elif option == "4":
            item_id = input("ID articulo a borrar: ").strip()
            if not validate_non_empty(item_id):
                print("Error vacio")
                continue
            delete_item(items, item_id)

        elif option == "5":
            list_items(items)

        else:
            print("Opción incorrecta")


if __name__ == "__main__":
    main()



# CONCLUSIONES

# Las funciones ayudaron a no hacer un solo codigo gigante
# y cada funcion sirve para una cosa entonces es mas facil entenderlo
# el diccionario es rapido y es mejor para buscar articulos
# hubo errores con entradas del usuario pero se puso validaciones,
# este CRUD se podria mejorar, guardando los datos en un archivo
# o en una base de datos y usar interfaz mas padre.


# REFERENCIAS

# 1 python docu de diccionario y listas
# 2 paginas webs de python
# 3 videos tutorial CRUD en Python ytube
