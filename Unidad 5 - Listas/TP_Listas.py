#1 Notas de 10 estudiantes
notas = [8, 7, 10, 4, 6, 9, 5, 8, 7, 6]

# Mostrar lista con estructura repetitiva
print("Notas de los estudiantes:")
for nota in notas:
    print(nota, end=" ")

# Calcular promedio
suma = 0
for nota in notas:
    suma += nota
promedio = suma / len(notas)
print(f"\nPromedio: {promedio}")

# Nota más alta y más baja
print(f"Nota más alta: {max(notas)}")
print(f"Nota más baja: {min(notas)}")

#2 Carga de productos
productos = []
for i in range(5):
    prod = input(f"Ingrese el producto {i+1}: ")
    productos.append(prod)

# Mostrar ordenado alfabéticamente
print("Lista ordenada:")
for p in sorted(productos):
    print(p)

# Eliminar producto
eliminar = input("¿Qué producto desea eliminar?: ")
if eliminar in productos:
    productos.remove(eliminar)
    print("Lista actualizada:")
    for p in productos:
        print(p)
else:
    print("El producto no existe.")
    
#3 Números al azar
import random

azar = [random.randint(1, 100) for _ in range(15)]
pares = []
impares = []

for num in azar:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f"Lista de pares ({len(pares)} números):", pares)
print(f"Lista de impares ({len(impares)} números):", impares)

#4 Sacar duplicados
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
unicos = []

for d in datos:
    if d not in unicos:
        unicos.append(d)

print("Lista sin repetidos:")
for u in unicos:
    print(u, end=" ")
    
#5 Asistencia de estudiantes
estudiantes = ["Ana", "Luis", "Marta", "Juan", "Pedro", "Sofía", "Elena", "Diego"]
opcion = input("¿Desea (A)gregar o (E)liminar un estudiante?: ").upper()

if opcion == "A":
    nuevo = input("Nombre del nuevo estudiante: ")
    estudiantes.append(nuevo)
elif opcion == "E":
    quitar = input("Nombre a eliminar: ")
    if quitar in estudiantes:
        estudiantes.remove(quitar)

print("Lista final:")
for e in estudiantes:
    print(e)


#6 Rotación a la derecha
numeros = [10, 20, 30, 40, 50, 60, 70]
ultimo = numeros.pop()
numeros.insert(0, ultimo)

print("Lista rotada:", numeros)

#7 Matriz de temperaturas
# [Min, Max]
temps = [[12, 22], [10, 25], [15, 28], [14, 20], [11, 24], [9, 19], [13, 26]]

suma_min = 0
suma_max = 0
max_amplitud = 0
dia_max_amp = 0

for i in range(len(temps)):
    minima, maxima = temps[i]
    suma_min += minima
    suma_max += maxima
    
    amplitud = maxima - minima
    if amplitud > max_amplitud:
        max_amplitud = amplitud
        dia_max_amp = i + 1

print(f"Promedio mínimas: {suma_min/7:.2f}")
print(f"Promedio máximas: {suma_max/7:.2f}")
print(f"Día de mayor amplitud térmica: Día {dia_max_amp}")

#8 Notas y materias
# 5 estudiantes, 3 materias
notas_matriz = [
    [8, 7, 9],
    [4, 5, 6],
    [10, 9, 10],
    [7, 7, 8],
    [6, 5, 7]
]

# Promedio por estudiante
for i in range(5):
    prom = sum(notas_matriz[i]) / 3
    print(f"Promedio estudiante {i+1}: {prom:.2f}")

# Promedio por materia
for j in range(3):
    suma_materia = 0
    for i in range(5):
        suma_materia += notas_matriz[i][j]
    print(f"Promedio materia {j+1}: {suma_materia/5:.2f}")


#9 Ta-Te-Ti
tablero = [["-" for _ in range(3)] for _ in range(3)]

for turno in range(2):
    jugador = "X" if turno % 2 == 0 else "O"
    f = int(input(f"Jugador {jugador}, fila (0-2): "))
    c = int(input(f"Jugador {jugador}, columna (0-2): "))
    tablero[f][c] = jugador
    
    for fila in tablero:
        print(" ".join(fila))

#10 Tienda de ventas
ventas = [
    [10, 12, 5, 7, 8, 15, 20], # Producto 1
    [5, 5, 5, 10, 10, 10, 10], # Producto 2
    [20, 15, 10, 5, 2, 1, 0],   # Producto 3
    [8, 8, 8, 8, 8, 8, 8]      # Producto 4
]

# Total por producto
totales_prod = []
for i in range(4):
    total = sum(ventas[i])
    totales_prod.append(total)
    print(f"Total producto {i+1}: {total}")

# Producto más vendido
print(f"Producto más vendido: {totales_prod.index(max(totales_prod)) + 1}")

# Día con mayores ventas
max_dia_venta = 0
dia_top = 0
for j in range(7):
    venta_dia = sum(ventas[i][j] for i in range(4))
    if venta_dia > max_dia_venta:
        max_dia_venta = venta_dia
        dia_top = j + 1
print(f"Día con mayores ventas totales: Día {dia_top}")

#11 Búsqueda de estudiante
nombres = ["Ana", "Juan", "Carla", "Dante", "Milo", "Fernando", "Roma", "Karina", "Lucas", "Bruno"]
buscar = input("Nombre a buscar: ")

if buscar in nombres:
    posicion = nombres.index(buscar)
    print(f"El nombre se encuentra en la posición: {posicion}")
else:
    print("El nombre no está en la lista.")


#12 Ordenar lista
numeros_usuario = []
for i in range(8):
    numeros_usuario.append(int(input(f"Número {i+1}: ")))

print("Original:", numeros_usuario)
print("Menor a mayor:", sorted(numeros_usuario))
print("Mayor a menor:", sorted(numeros_usuario, reverse=True))


#13 Ranking de videojuego
puntajes = [450, 1200, 875, 990, 300, 1500, 640]

print(f"Máximo: {max(puntajes)}, Mínimo: {min(puntajes)}")

ranking = sorted(puntajes, reverse=True)
print("Ranking:", ranking)

pos = ranking.index(990) + 1
print(f"El puntaje 990 está en la posición {pos} del ranking.")