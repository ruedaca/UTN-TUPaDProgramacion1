#Inicialización
herramientas = []
existencias = []

# Control del bucle principal para el menú
continuar = True

while continuar:
    print("\n--- SISTEMA DE CONTROL DE INVENTARIO ---")
    print("1. Carga Inicial de Herramientas")
    print("2. Carga de Existencias")
    print("3. Visualización de Inventario")
    print("4. Consulta de Stock")
    print("5. Reporte de Agotados")
    print("6. Alta de Nuevo Producto")
    print("7. Actualización de Stock (Venta/Ingreso)")
    print("8. Salir")
    
    opcion = input("Seleccione una opción: ")

    # 1. Carga Inicial de Herramientas
    if opcion == "1":
        cantidad = int(input("¿Cuántas herramientas desea cargar?: "))
        contador = 0
        while contador < cantidad:
            nombre = input(f"Ingrese el nombre de la herramienta {contador + 1}: ").strip()
            
            # Validación de nombre vacío o duplicado
            if nombre == "":
                print("Error: El nombre no puede estar vacío.")
            else:
                duplicado = False
                for h in herramientas:
                    if h.lower() == nombre.lower():
                        duplicado = True
                
                if duplicado:
                    print("Error: La herramienta ya existe.")
                else:
                    herramientas.append(nombre)
                    # Inicializamos en 0 para mantener sincronía 
                    existencias.append(0)
                    contador += 1

    # 2. Carga de Existencias
    elif opcion == "2":
        if len(herramientas) == 0:
            print("Error: No hay herramientas cargadas. Use la opción 1.")
        else:
            for i in range(len(herramientas)):
                print(f"Herramienta: {herramientas[i]}")
                cantidad_stock = int(input(f"Ingrese unidades para {herramientas[i]}: "))
                # Validación de números positivos
                while cantidad_stock < 0:
                    print("Error: El stock no puede ser negativo.")
                    cantidad_stock = int(input(f"Reingrese para {herramientas[i]}: "))
                existencias[i] = cantidad_stock

    # 3. Visualización de Inventario
    elif opcion == "3":
        print("\n--- INVENTARIO ---")
        for i in range(len(herramientas)):
            print(f"Producto: {herramientas[i]} | Stock: {existencias[i]}")

    # 4. Consulta de Stock
    elif opcion == "4":
        busqueda = input("Nombre de la herramienta a buscar: ").strip()
        encontrado = False
        for i in range(len(herramientas)):
            if herramientas[i].lower() == busqueda.lower():
                print(f"Stock disponible de {herramientas[i]}: {existencias[i]}")
                encontrado = True
        if not encontrado:
            print("La herramienta no existe en el catálogo.")

    # 5. Reporte de Agotados
    elif opcion == "5":
        print("\n--- PRODUCTOS AGOTADOS ---")
        hay_agotados = False
        for i in range(len(herramientas)):
            if existencias[i] == 0:
                print(f"- {herramientas[i]}")
                hay_agotados = True
        if not hay_agotados:
            print("No hay productos con stock en cero.")

    # 6. Alta de Nuevo Producto
    elif opcion == "6":
        nuevo_nombre = input("Nombre del nuevo producto: ").strip()
        
        # Validaciones de duplicados y vacíos
        duplicado = False
        for h in herramientas:
            if h.lower() == nuevo_nombre.lower():
                duplicado = True
        
        if nuevo_nombre == "":
            print("Error: Nombre vacío. Volviendo al menú.")
        elif duplicado:
            print("Error: Producto duplicado. Volviendo al menú.")
        else:
            nuevo_stock = int(input("Ingrese stock inicial: "))
            if nuevo_stock < 0:
                print("Error: Existencia negativa. Volviendo al menú.")
            else:
                herramientas.append(nuevo_nombre)
                existencias.append(nuevo_stock)
                print("Producto agregado con éxito.")

    # 7. Actualización de Stock (Venta/Ingreso)
    elif opcion == "7":
        herramienta_act = input("Herramienta a actualizar: ").strip()
        indice = -1
        for i in range(len(herramientas)):
            if herramientas[i].lower() == herramienta_act.lower():
                indice = i
        
        if indice == -1:
            print("Error: La herramienta no existe.")
        else:
            tipo = input("¿Es (V)enta o (I)ngreso?: ").upper()
            cantidad_mov = int(input("Cantidad: "))
            
            if tipo == "I":
                existencias[indice] += cantidad_mov
            elif tipo == "V":
                # Impedir ventas que superen el stock disponible
                if existencias[indice] >= cantidad_mov:
                    existencias[indice] -= cantidad_mov
                else:
                    print("Error: Stock insuficiente para realizar la venta.")
            else:
                print("Opción de movimiento no válida.")

    # 8. Salir
    elif opcion == "8":
        print("Saliendo del sistema...")
        continuar = False
        
    else:
        print("Opción no reconocida, intente de nuevo.")