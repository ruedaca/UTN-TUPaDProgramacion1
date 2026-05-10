# 1) Mensaje de bienvenida
print("Hola Mundo!")

# 2) Saludo personalizado
nombre = input("Ingresa tu nombre: ")
print(f"Hola {nombre}!")

# 3) Ficha de datos personales
nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
residencia = input("Lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# 4) Cálculo de círculo (Área y Perímetro)
import math
radio = float(input("Ingresa el radio del círculo: "))
area = math.pi * radio**2
perimetro = 2 * math.pi * radio
print(f"Área: {area:.2f}")
print(f"Perímetro: {perimetro:.2f}")

# 5) Conversión de segundos a horas
segundos = float(input("Ingresa la cantidad de segundos: "))
horas = segundos / 3600
print(f"Equivale a {horas:.2f} horas")

# 6) Tabla de multiplicar
num = int(input("Ingresa un número para ver su tabla: "))
print(f"Tabla del {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# 7) Operaciones matemáticas básicas
n1 = float(input("Ingresa el primer número: "))
n2 = float(input("Ingresa el segundo número: "))
print(f"Suma: {n1 + n2}")
print(f"Resta: {n1 - n2}")
print(f"Multiplicación: {n1 * n2}")
print(f"División: {n1 / n2}")

# 8) Índice de Masa Corporal (IMC)
peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))
imc = peso / (altura**2)
print(f"Tu índice de masa corporal es: {imc:.2f}")

# 9) Conversión de Celsius a Fahrenheit
celsius = float(input("Ingresa la temperatura en Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C equivale a {fahrenheit}°F")

# 10) Promedio de tres números
n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))
n3 = float(input("Número 3: "))
promedio = (n1 + n2 + n3) / 3
print(f"El promedio es: {promedio:.2f}")