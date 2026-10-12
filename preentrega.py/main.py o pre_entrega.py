# Lista principal donde se almacenarán los productos
# Cada producto será una sublista: [nombre, categoría, precio]
productos = []

# Bucle principal del programa
while True:
    # -------------------------------------------------------------------------
    # Menú de opciones
    # -------------------------------------------------------------------------
    print("\n" + "=" * 40)
    print(" Sistema de Gestión Básica de Productos")
    print("=" * 40)
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    print("=" * 40)

    opcion = input("Seleccione una opción (1-5): ").strip()

    # -------------------------------------------------------------------------
    # Opción 1: Agregar producto
    # -------------------------------------------------------------------------
    if opcion == "1":
        print("\n--- Agregar Producto ---")

        # Validación del nombre (no vacío)
        while True:
            nombre = input("Ingrese el nombre del producto: ").strip()
            if nombre != "":
                break
            print("❌ El nombre no puede estar vacío. Intente nuevamente.")

        # Validación de la categoría (no vacía)
        while True:
            categoria = input("Ingrese la categoría del producto: ").strip()
            if categoria != "":
                break
            print("❌ La categoría no puede estar vacía. Intente nuevamente.")

        # Validación del precio (número entero válido y positivo, sin centavos)
        while True:
            precio_input = input("Ingrese el precio (sin centavos): ").strip()
            if precio_input.isdigit():
                precio = int(precio_input)
                if precio >= 0:
                    break
                else:
                    print("❌ El precio debe ser mayor o igual a 0.")
            else:
                print("❌ Ingrese un número entero válido.")

        # Se agrega el producto como sublista [nombre, categoría, precio]
        nuevo_producto = [nombre, categoria, precio]
        productos.append(nuevo_producto)
        print(f"\n✅ Producto '{nombre}' agregado con éxito.")

    # -------------------------------------------------------------------------
    # Opción 2: Mostrar productos
    # -------------------------------------------------------------------------
    elif opcion == "2":
        print("\n--- Lista de Productos Registrados ---")

        if len(productos) == 0:
            print("ℹ️ No hay productos registrados en el sistema.")
        else:
            # Recorremos la lista de productos con enumerate para obtener el índice numerado
            for i in range(len(productos)):
                prod = productos[i]
                num = i + 1
                nombre_p = prod[0]
                categoria_p = prod[1]
                precio_p = prod[2]

                print(
                    f"{num}. Nombre: {nombre_p} | Categoría: {categoria_p} | Precio: ${precio_p}"
                )

    # -------------------------------------------------------------------------
    # Opción 3: Buscar producto por nombre
    # -------------------------------------------------------------------------
    elif opcion == "3":
        print("\n--- Buscar Producto ---")

        if len(productos) == 0:
            print("ℹ️ No hay productos registrados para buscar.")
        else:
            # Validación del término de búsqueda
            while True:
                busqueda = (
                    input("Ingrese el nombre del producto a buscar: ")
                    .strip()
                    .lower()
                )
                if busqueda != "":
                    break
                print("❌ El término de búsqueda no puede estar vacío.")

            coincidencias = 0

            print("\nResultados de la búsqueda:")
            for i in range(len(productos)):
                prod = productos[i]
                nombre_p = prod[0]

                # Búsqueda que permite coincidencia parcial (no sensible a mayúsculas/minúsculas)
                if busqueda in nombre_p.lower():
                    coincidencias += 1
                    print(
                        f"• {coincidencias}. Nombre: {nombre_p} | Categoría: {prod[1]} | Precio: ${prod[2]}"
                    )

            if coincidencias == 0:
                print(
                    f"❌ No se encontraron productos que coincidan con '{busqueda}'."
                )

    # -------------------------------------------------------------------------
    # Opción 4: Eliminar producto
    # -------------------------------------------------------------------------
    elif opcion == "4":
        print("\n--- Eliminar Producto ---")

        if len(productos) == 0:
            print("ℹ️ No hay productos registrados para eliminar.")
        else:
            # Se muestran los productos con su número de posición
            print("Productos disponibles para eliminar:")
            for i in range(len(productos)):
                print(
                    f"{i + 1}. {productos[i][0]} (Categoría: {productos[i][1]})"
                )

            # Validación de la selección por número de posición
            while True:
                posicion_input = input(
                    "\nIngrese el número del producto a eliminar: "
                ).strip()

                if posicion_input.isdigit():
                    posicion = int(posicion_input)
                    # Se verifica que la posición seleccionada sea válida en la lista
                    if 1 <= posicion <= len(productos):
                        # Se ajusta la posición de base 1 a base 0 para listas de Python
                        indice = posicion - 1
                        producto_eliminado = productos.pop(indice)
                        print(
                            f"\n✅ Producto '{producto_eliminado[0]}' eliminado correctamente."
                        )
                        break
                    else:
                        print("❌ El número ingresado está fuera de rango.")
                else:
                    print("❌ Debe ingresar un número entero válido.")

    # -------------------------------------------------------------------------
    # Opción 5: Salir
    # -------------------------------------------------------------------------
    elif opcion == "5":
        print("\n👋 ¡Gracias por utilizar el sistema! Hasta luego.")
        break

    # -------------------------------------------------------------------------
    # Opción inválida
    # -------------------------------------------------------------------------
    else:
        print("❌ Opción no válida. Por favor, ingrese un número del 1 al 5.")