#Ejercicio 1: Saludo
def imprimir_hola_mundo():
    print("Hola Mundo!")

# Programa principal
imprimir_hola_mundo()

#Ejercicio 2: Saludo personalizado
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# Programa principal
nombre_ingresado = input("Ingresá tu nombre: ")
mensaje = saludar_usuario(nombre_ingresado)
print(mensaje)

#Ejercicio 3: Información personal
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Programa principal
nom = input("Nombre: ")
ape = input("Apellido: ")
ed = input("Edad: ")
res = input("Ciudad de residencia: ")

informacion_personal(nom, ape, ed, res)

#Ejercicio 4: Área y perímetro
import math

def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# Programa principal
r = float(input("Ingresá el radio del círculo: "))
print(f"Área: {calcular_area_circulo(r):.2f}")
print(f"Perímetro: {calcular_perimetro_circulo(r):.2f}")

#Ejercicio 5: Conversión de Segundos a Horas
def segundos_a_horas(segundos):
    return segundos / 3600

# Programa principal
seg = float(input("Cantidad de segundos: "))
print(f"Equivale a {segundos_a_horas(seg):.2f} horas.")


#Ejercicio 6: Tabla de Multiplicar
def tabla_multiplicar(numero):
    print(f"--- Tabla del {numero} ---")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Programa principal
num = int(input("¿De qué número querés la tabla?: "))
tabla_multiplicar(num)


#Ejercicio 7: Operaciones Básicas (Tuplas)
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multi = a * b
    div = a / b if b != 0 else "Error (división por cero)"
    return (suma, resta, multi, div)

# Programa principal
n1 = float(input("Número A: "))
n2 = float(input("Número B: "))
s, r, m, d = operaciones_basicas(n1, n2)

print(f"Suma: {s} | Resta: {r} | Multiplicación: {m} | División: {d}")


#Ejercicio 8: Calcular IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Programa principal
p = float(input("Peso (kg): "))
alt = float(input("Altura (m): "))
resultado_imc = calcular_imc(p, alt)
print(f"Tu IMC es: {resultado_imc:.2f}")


#Ejercicio 9: Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 1.8) + 32

# Programa principal
c = float(input("Grados Celsius: "))
print(f"{c}°C equivalen a {celsius_a_fahrenheit(c):.1f}°F")

#Ejercicio 10: Promedio de Tres Números
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Programa principal
val1 = float(input("Primer número: "))
val2 = float(input("Segundo número: "))
val3 = float(input("Tercer número: "))
print(f"El promedio es: {calcular_promedio(val1, val2, val3):.2f}")