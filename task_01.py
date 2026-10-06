#Operadores aritmeticos
print (f"suma = 10 + 15 = {10 + 15}")
print (f"resta = 10 - 5 = {10 - 5}")
print (f"multiplicacion = 10 * 6 = {10 * 6}")
print (f"division = 10 / 2 = {10 / 2}")
print (f"division_entera = 10 // 3 = {10 // 3}")
print (f"modulo = 10 % 3 = {10 % 3}")     #EL RESIDUO DE LA DIVISION
print (f"exponente = 10 ** 2 = {10 ** 2}")
# Operadores de comparación
print("Operadores de Comparación:")
print(f"Igualdad: 13 == 7 es {13 == 7}")
print(f"Desigualdad: 13 != 7 es {13 != 7}")
print(f"Mayor que: 13 > 7 es {13 > 7}")
print(f"Menor que: 13 < 7 es {13 < 7}")
print(f"Mayopr o igual: 13 >= 7 es {13 >= 7}")
print(f"Menor o igual: 13 <= 7 es {13 <= 7}")

# Operadores de asignación

print("Operadores de Asignación:")
number =13  # Asignación
print(f"Valor inicial: {number}")
number += 7  # Suma y asignación
print(f"Después de += 7: {number}")
number -= 7  # Resta y asignación
print(f"Después de -= 7: {number}")
number *= 7  # Multiplicación y asignación
print(f"Después de *= 7: {number}")
number /= 7  # División y asignación
print(f"Después de /= 7: {number}")
number //= 7  # División entera y asignación
print(f"Después de //= 7: {number}")
number %= 7  # Módulo y asignación
print(f"Después de %= 7: {number}")
number **= 7  # Exponente y asignación
print(f"Después de **= 7: {number}")

# Operadores de Identidad
print("Operadores de Identidad:")
new_number = number  # Asignación de new_number a number
print(f"number is new_number: {number is new_number}") # El operador "is" verifica si ambos objetos son el mismo en memoria, es decir, si apuntan al mismo objeto. En este caso, como new_number se asigna a number, ambos apuntan al mismo objeto en memoria, por lo que devuelve True.
print(f"number is not new_number: {number is not new_number}") # a diferencia de != lo que "is not" hace es verificar si ambos objetos no son el mismo en memoria, es decir, si no apuntan al mismo objeto. En este caso, como new_number se asigna a number, ambos apuntan al mismo objeto en memoria, por lo que devuelve False.

# Operadores de Pertenencia
print("Operadores de Pertenencia:")
print(f"'Y' in 'Python' = {'y' in 'python'}") # verifica si la letra 'y' está presente en la palabra 'python', y devuelve True o False dependiendo del resultado
print(f"'B' not in 'Python' = {'b' not in 'python'}") # verifica si la letra 'b' no está presente en la palabra 'python', y devuelve True o False dependiendo del resultado

# Operadores de bit
print("Operadores de Bit:") # se utilizan para manipular los números enteros a nivel de sus bits individuales (ceros y unos) en su representación binaria
#AND: Devuelve 1 en cada posición si ambos bits correspondientes son 1.
print(f"AND: 13 & 7 = {13 & 7}")  # 13 en bit es 1101 y 7 en bit es 0111, el resultado es 0101 que es 5 en decimal
# OR: Devuelve 1 en cada posición si al menos uno de los bits correspondientes es 1.
print(f"OR: 13 | 7 = {13 | 7}") # 13 en bit es 1101 y 7 en bit es 0111, el resultado es 1111 que es 15 en decimal
# XOR: Devuelve 1 en cada posición si los bits correspondientes son diferentes.
print(f"XOR: 13 ^ 7 = {13 ^ 7}") # 13 en bit es 1101 y 7 en bit es 0111, el resultado es 1010 que es 10 en decimal
# NOT: Invierte los bits, cambiando 1 a 0 y 0 a 1.
print(f"NOT: ~ 13 = {~13}") # 13 en bit es 1101, el resultado es 0010 que es -14 en decimal (en complemento a dos)
# Desplazamiento de bits: Mueve los bits hacia la izquierda o hacia la derecha.
print(f"Desplazamiento a la izquierda: 13 << 2 = {13 << 2}") # 13 en bit es 1101, el resultado es 110100 que es 52 en decimal
# Desplazamiento a la derecha: Mueve los bits hacia la derecha, eliminando los bits menos significativos.   
print(f"Desplazamiento a la derecha: 13 >> 2 = {13 >> 2}") # 13 en bit es 1101, el resultado es 11 que es 3 en decimal

"""
Estructuras de control:
- Condicionales: if, elif, else
- Iterativas: for, while
- Excepciones: try, except, finally
"""

# Condicionales
print("Condicionales:")
my_string = 'Python'
if my_string == 'Python':
    print("La cadena es Python")
elif my_string == 'Java':
    print("La cadena es Java")
else:
    print("La cadena no es Python ni Java")

# Iterativas
print("Iterativas")

for i in range(11):
     print(i)

i = 0
while i <= 11:
    print(i)
    i += 1
    
# Manejo de Excepciones
print("Manejo de Excepciones:")
try:
    print(10 / 0)
except ZeroDivisionError:
    print("No se puede dividir por cero")
finally:
    print("Finalizó el manjeo de excepciones")


    # reto
for numero in range(10, 56):
    if numero % 2 == 0 and numero % 3 != 0 and numero != 16:
        print(numero)
