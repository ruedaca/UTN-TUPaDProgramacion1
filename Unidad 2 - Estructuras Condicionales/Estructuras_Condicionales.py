# 1) Verificación de mayoría de edad
edad = int(input("Ingresa tu edad: "))
if edad > 18:
    print("Es mayor de edad")

# 2) Sistema de aprobación
nota = float(input("Ingresa tu nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# 3) Filtro de números pares
numero = int(input("Ingresa un número par: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# 4) Categorías por edad
edad_cat = int(input("Ingresa tu edad para categorizarte: "))
if edad_cat < 12:
    print("Niño/a")
elif 12 <= edad_cat < 18:
    print("Adolescente")
elif 18 <= edad_cat < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

# 5) Validación de longitud de contraseña
password = input("Ingresa una contraseña (8 a 14 caracteres): ")
largo = len(password)
if 8 <= largo <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# 6) Categoría de consumo eléctrico
consumo = float(input("Ingresa el consumo mensual en kWh: "))
if consumo < 150:
    print("Consumo bajo")
elif 150 <= consumo <= 300:
    print("Consumo medio")
else:
    print("Consumo alto")

if consumo > 500:
    print("Considere medidas de ahorro energético")

# 7) Detector de vocales al final
texto = input("Ingresa una palabra o frase: ")
# Convertimos a minúscula para comparar más fácil
if texto.lower().endswith(('a', 'e', 'i', 'o', 'u')):
    print(texto + "!")
else:
    print(texto)

# 8) Transformador de nombres
nombre = input("Ingresa tu nombre: ")
print("Opciones: 1. MAYÚSCULAS | 2. minúsculas | 3. Primera Mayúscula")
opcion = input("Elige una opción (1, 2 o 3): ")

if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())

# 9) Escala de Richter para terremotos
magnitud = float(input("Ingresa la magnitud del terremoto: "))
if magnitud < 3:
    print("Muy leve")
elif 3 <= magnitud < 4:
    print("Leve")
elif 4 <= magnitud < 5:
    print("Moderado")
elif 5 <= magnitud < 6:
    print("Fuerte")
elif 6 <= magnitud < 7:
    print("Muy Fuerte")
else:
    print("Extremo")

# 10) Determinación de estación del año
hemisferio = input("¿En qué hemisferio estás? (N/S): ").upper()
mes = int(input("Número de mes (1-12): "))
dia = int(input("Día del mes: "))

# Primero determinamos el periodo según la fecha
if (mes == 12 and dia >= 21) or (mes <= 2) or (mes == 3 and dia <= 20):
    p = "P1" # 21 Dic a 20 Mar
elif (mes == 3 and dia >= 21) or (mes <= 5) or (mes == 6 and dia <= 20):
    p = "P2" # 21 Mar a 20 Jun
elif (mes == 6 and dia >= 21) or (mes <= 8) or (mes == 9 and dia <= 20):
    p = "P3" # 21 Jun a 20 Sep
else:
    p = "P4" # 21 Sep a 20 Dic

# Ahora asignamos estación según hemisferio
if hemisferio == "N":
    estaciones = {"P1": "Invierno", "P2": "Primavera", "P3": "Verano", "P4": "Otoño"}
else:
    estaciones = {"P1": "Verano", "P2": "Otoño", "P3": "Invierno", "P4": "Primavera"}

print(f"Te encuentras en: {estaciones[p]}")