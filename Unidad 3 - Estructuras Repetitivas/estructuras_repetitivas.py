# Actividad 1
# Recorremos los números desde 0 hasta 100 (inclusive)
for numero in range(0, 101):
    # Imprimimos cada número en una línea
    print(numero)

# Actividad 2
# Pedimos al usuario que ingrese un número entero
numero = int(input("Ingresá un número entero: "))

# Convertimos el número a string para contar sus dígitos
cantidad_digitos = len(str(abs(numero)))  
# abs() evita problemas si el número es negativo

# Mostramos el resultado
print("La cantidad de dígitos es:", cantidad_digitos)

# Actividad 3
# Pedimos los dos números al usuario
inicio = int(input("Ingresá el primer número: "))
fin = int(input("Ingresá el segundo número: "))

# Inicializamos la suma
suma = 0

# Recorremos los números entre ambos (sin incluirlos)
for numero in range(inicio + 1, fin):
    suma += numero  # Sumamos cada número

# Mostramos el resultado
print("La suma es:", suma)

# Actividad 4
suma_total = 0

while True:
    # Pedimos un número al usuario
    numero = int(input("Ingresá un número (0 para terminar): "))
    
    # Si el número es 0, salimos del bucle
    if numero == 0:
        break
    
    # Sumamos el número ingresado
    suma_total += numero

# Mostramos el total acumulado
print("La suma total es:", suma_total)

# Actividad 5
import random  # Importamos el módulo random

# Generamos un número aleatorio entre 0 y 9
numero_secreto = random.randint(0, 9)

intentos = 0

while True:
    # Pedimos al usuario que adivine el número
    intento = int(input("Adiviná el número (0 a 9): "))
    intentos += 1
    
    # Comparamos el número ingresado con el secreto
    if intento == numero_secreto:
        print("¡Correcto!")
        break
    else:
        print("Incorrecto, intentá de nuevo.")

# Mostramos la cantidad de intentos
print("Cantidad de intentos:", intentos)

# Actividad 6
# Recorremos los números desde 100 hasta 0, de a -1
for numero in range(100, -1, -1):
    # Verificamos si el número es par
    if numero % 2 == 0:
        print(numero)

# Actividad 7
# Pedimos un número entero positivo
numero = int(input("Ingresá un número entero positivo: "))

suma = 0

# Sumamos todos los números desde 0 hasta el número ingresado
for i in range(0, numero + 1):
    suma += i

# Mostramos el resultado
print("La suma es:", suma)

# Actividad 8
# Cantidad de números a ingresar (cambiando este valor funciona para 100)
cantidad = 100

pares = impares = positivos = negativos = 0

for i in range(cantidad):
    numero = int(input(f"Ingresá el número {i + 1}: "))
    
    # Verificamos si es par o impar
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    # Verificamos si es positivo o negativo
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

# Mostramos los resultados
print("Pares:", pares)
print("Impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)

# Actividad 9
cantidad = 100
suma = 0

for i in range(cantidad):
    numero = int(input(f"Ingresá el número {i + 1}: "))
    suma += numero

# Calculamos la media
media = suma / cantidad

# Mostramos el resultado
print("La media es:", media)

# Actividad 10
# Pedimos el número al usuario
numero = input("Ingresá un número: ")

# Invertimos el número usando slicing
numero_invertido = numero[::-1]

# Mostramos el resultado
print("Número invertido:", numero_invertido)
