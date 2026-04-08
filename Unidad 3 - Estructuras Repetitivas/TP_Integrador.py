#Ejercicio 1: Caja del Kiosco
# 1. Pedir nombre del cliente (solo letras, validar con isalpha())
nombre = input("Cliente: ")
while not nombre.isalpha() or nombre == "":
    print("Error: Ingrese un nombre válido (solo letras y no vacío).")
    nombre = input("Cliente: ")

# 2. Pedir cantidad de productos (entero positivo)
cant_str = input("Cantidad de productos a comprar: ")
while not cant_str.isdigit() or int(cant_str) <= 0:
    print("Error: Ingrese un número entero mayor a 0.")
    cant_str = input("Cantidad de productos a comprar: ")

cantidad_productos = int(cant_str)
total_sin_descuento = 0
total_con_descuento = 0

# 3. Proceso por cada producto
for i in range(1, cantidad_productos + 1):
    print(f"Producto {i}")
    
    # Pedir y validar precio
    precio_str = input("Precio: ")
    while not precio_str.isdigit():
        print("Error: Ingrese un precio válido.")
        precio_str = input("Precio: ")
    precio = int(precio_str)
    
    total_sin_descuento += precio
    
    # Pedir y validar descuento
    tiene_desc = input("¿Tiene descuento? (S/N): ").lower()
    while tiene_desc != "s" and tiene_desc != "n":
        print("Error: Ingrese S o N.")
        tiene_desc = input("¿Tiene descuento? (S/N): ").lower()
    
    if tiene_desc == "s":
        # Aplicar 10% de descuento
        precio_final = precio * 0.90
    else:
        precio_final = precio
        
    total_con_descuento += precio_final

# 4. Cálculos finales y salida
ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad_productos

print(f"\nTotal sin descuentos: ${total_sin_descuento}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro total: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")

#Ejercicio 2 — Acceso al Campus y Menú Seguro
# 1. Credenciales fijas
USUARIO_CORRECTO = "alumno"
CLAVE_CORRECTA = "python123"

intentos = 0
acceso = False

# 2. Control de intentos de login
while intentos < 3 and not acceso:
    intentos += 1
    print(f"Intento {intentos}/3")
    user_input = input("Usuario: ")
    pass_input = input("Clave: ")
    
    if user_input == USUARIO_CORRECTO and pass_input == CLAVE_CORRECTA:
        acceso = True
        print("Acceso concedido.")
    else:
        print("Error: credenciales inválidas.")

# 3. Manejo de bloqueo o ingreso al menú
if not acceso:
    print("Cuenta bloqueada.")
else:
    opcion = ""
    while opcion != "4":
        print("\n1) Estado 2) Cambiar clave 3) Mensaje 4) Salir")
        opcion = input("Opción: ")
        
        # Validación de menú (.isdigit() y rango 1-4)
        if not opcion.isdigit():
            print("Error: ingrese un número válido.")
        elif int(opcion) < 1 or int(opcion) > 4:
            print("Error: opción fuera de rango.")
        else:
            if opcion == "1":
                print("Inscripto")
            elif opcion == "2":
                # Cambio de clave con validación de longitud
                nueva_clave = input("Nueva clave: ")
                while len(nueva_clave) < 6:
                    print("Error: mínimo 6 caracteres.")
                    nueva_clave = input("Nueva clave: ")
                
                confirmacion = input("Confirme nueva clave: ")
                if nueva_clave == confirmacion:
                    CLAVE_CORRECTA = nueva_clave
                    print("Clave cambiada con éxito.")
                else:
                    print("Error: las claves no coinciden.")
            elif opcion == "3":
                print("El éxito es la suma de pequeños esfuerzos repetidos día tras día.")
            elif opcion == "4":
                print("Saliendo del sistema...")
                

#Ejercicio 3: Agenda de Turnos con Nombres (sin listas)
# 1. Pedir nombre del operador
operador = input("Nombre del operador: ")
while not operador.isalpha():
    print("Error: Solo letras.")
    operador = input("Nombre del operador: ")

# Inicialización de turnos (Lunes: 4, Martes: 3)
lunes1 = ""; lunes2 = ""; lunes3 = ""; lunes4 = ""
martes1 = ""; martes2 = ""; martes3 = ""

opcion_menu = ""
while opcion_menu != "5":
    print("\n1. Reservar | 2. Cancelar | 3. Ver Agenda | 4. Resumen | 5. Salir")
    opcion_menu = input("Opción: ")
    
    if opcion_menu == "1":
        dia = input("Día (1=Lunes, 2=Martes): ")
        while dia != "1" and dia != "2":
            dia = input("Error. Elija 1 o 2: ")
        
        paciente = input("Nombre del paciente: ")
        while not paciente.isalpha():
            paciente = input("Error: Solo letras. Nombre: ")

        # Lógica de reserva por día
        if dia == "1":
            if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                print("Error: Paciente ya tiene turno este día.")
            elif lunes1 == "": lunes1 = paciente; print("Reservado en Turno 1")
            elif lunes2 == "": lunes2 = paciente; print("Reservado en Turno 2")
            elif lunes3 == "": lunes3 = paciente; print("Reservado en Turno 3")
            elif lunes4 == "": lunes4 = paciente; print("Reservado en Turno 4")
            else: print("Día Lunes lleno.")
        else:
            if paciente == martes1 or paciente == martes2 or paciente == martes3:
                print("Error: Paciente ya tiene turno este día.")
            elif martes1 == "": martes1 = paciente; print("Reservado en Turno 1")
            elif martes2 == "": martes2 = paciente; print("Reservado en Turno 2")
            elif martes3 == "": martes3 = paciente; print("Reservado en Turno 3")
            else: print("Día Martes lleno.")

    elif opcion_menu == "2":
        dia = input("Día a cancelar (1 o 2): ")
        paciente = input("Nombre del paciente: ")
        if dia == "1":
            if lunes1 == paciente: lunes1 = ""
            elif lunes2 == paciente: lunes2 = ""
            elif lunes3 == paciente: lunes3 = ""
            elif lunes4 == paciente: lunes4 = ""
            print("Turno cancelado si existía.")
        else:
            if martes1 == paciente: martes1 = ""
            elif martes2 == paciente: martes2 = ""
            elif martes3 == paciente: martes3 = ""
            print("Turno cancelado si existía.")

    elif opcion_menu == "3":
        dia = input("Ver agenda (1=Lunes, 2=Martes): ")
        if dia == "1":
            print(f"1. {lunes1 if lunes1 != '' else '(libre)'}")
            print(f"2. {lunes2 if lunes2 != '' else '(libre)'}")
            print(f"3. {lunes3 if lunes3 != '' else '(libre)'}")
            print(f"4. {lunes4 if lunes4 != '' else '(libre)'}")
        else:
            print(f"1. {martes1 if martes1 != '' else '(libre)'}")
            print(f"2. {martes2 if martes2 != '' else '(libre)'}")
            print(f"3. {martes3 if martes3 != '' else '(libre)'}")

    elif opcion_menu == "4":
        # Conteo manual sin listas
        occ_lunes = 0
        if lunes1 != "": occ_lunes += 1
        if lunes2 != "": occ_lunes += 1
        if lunes3 != "": occ_lunes += 1
        if lunes4 != "": occ_lunes += 1
        
        occ_martes = 0
        if martes1 != "": occ_martes += 1
        if martes2 != "": occ_martes += 1
        if martes3 != "": occ_martes += 1
        
        print(f"Lunes: {occ_lunes} ocupados, {4-occ_lunes} libres.")
        print(f"Martes: {occ_martes} ocupados, {3-occ_martes} libres.")
        if occ_lunes > occ_martes: print("Día con más turnos: Lunes")
        elif occ_martes > occ_lunes: print("Día con más turnos: Martes")
        else: print("Empate en ocupación.")
        
        
#Ejercicio 4: Escape Room: La Bóveda
# Variables iniciales
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
racha_forzar = 0 # Para regla anti-spam

nombre_agente = input("Nombre del agente: ")
while not nombre_agente.isalpha():
    nombre_agente = input("Error: Solo letras. Nombre: ")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not (alarma and tiempo <= 3):
    print(f"\n--- ESTADO: E:{energia} | T:{tiempo} | Cerraduras:{cerraduras_abiertas} | Alarma:{alarma} ---")
    print("1. Forzar | 2. Hackear | 3. Descansar")
    opc = input("Acción: ")
    while not opc.isdigit(): opc = input("Use números: ")

    if opc == "1":
        racha_forzar += 1
        energia -= 20
        tiempo -= 2
        
        if racha_forzar >= 3:
            alarma = True
            print("¡La cerradura se trabó por insistir! Alarma activa.")
        else:
            if energia < 40:
                riesgo = input("Riesgo de alarma. Elija 1-3: ")
                if riesgo == "3": alarma = True
            
            if not alarma:
                cerraduras_abiertas += 1
                print("¡Cerradura abierta!")

    elif opc == "2":
        racha_forzar = 0
        energia -= 10
        tiempo -= 3
        for i in range(4):
            print("Hackeando...")
            codigo_parcial += "A"
        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("Sistema vulnerado: Cerradura abierta.")

    elif opc == "3":
        racha_forzar = 0
        energia += 15
        if energia > 100: energia = 100
        tiempo -= 1
        if alarma: energia -= 10
        print("Descansando...")

# Finalización
if cerraduras_abiertas == 3: print("¡VICTORIA!")
elif alarma and tiempo <= 3: print("DERROTA: Sistema bloqueado por alarma.")
else: print("DERROTA: Sin recursos.")


#Ejercicio 5: La Arena del Gladiador
# Paso 1: Configuración
nombre = input("Nombre del Gladiador: ")
while not nombre.isalpha() or nombre == "":
    print("Error: Solo se permiten letras")
    nombre = input("Nombre del Gladiador: ")

# Paso 2: Estadísticas
hp_jugador = 100
hp_enemigo = 100
pociones = 3
ataque_pesado_base = 15
ataque_enemigo = 12

# Paso 3: Ciclo de Combate
while hp_jugador > 0 and hp_enemigo > 0:
    print(f"\n{nombre} (HP: {hp_jugador}) vs Enemigo (HP: {hp_enemigo}) | Pociones: {pociones}")
    print("1. Ataque Pesado | 2. Ráfaga Veloz | 3. Curar")
    
    opcion = input("Opción: ")
    while not opcion.isdigit() or opcion not in ["1", "2", "3"]:
        print("Error: Ingrese un número válido (1, 2 o 3).")
        opcion = input("Opción: ")

    # Acciones del Jugador
    if opcion == "1":
        daño = float(ataque_pesado_base)
        if hp_enemigo < 20:
            daño *= 1.5
            print("¡GOLPE CRÍTICO!")
        hp_enemigo -= int(daño)
        print(f"¡Atacaste por {daño} puntos!")

    elif opcion == "2":
        print(">> ¡Inicias una ráfaga de golpes!")
        for _ in range(3):
            hp_enemigo -= 5
            print("> Golpe conectado por 5 de daño")

    elif opcion == "3":
        if pociones > 0:
            hp_jugador += 30
            pociones -= 1
            print("Te has curado.")
        else:
            print("¡No quedan pociones! Pierdes el turno.")

    # Turno del Enemigo (si sigue vivo)
    if hp_enemigo > 0:
        hp_jugador -= ataque_enemigo
        print(f"¡El enemigo te atacó por {ataque_enemigo} puntos!")

# Paso 4: Fin del Juego
if hp_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado.")
else:
    print("DERROTA. Has caído en combate.")