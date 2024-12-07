# Programa 10/Bloque 4
### Al fin
- Este programa usa de base el programa 9
- Pero en este caso utilizamos l while para verificar si el usuario descea salir del programa
```python
def es_primo(num):
    if num < 2:
        return False  # Los números menores que 2 no son primos
    for i in range(2, int(num ** 0.5) + 1):  # Comprobar divisibilidad hasta la raíz cuadrada del número
        if num % i == 0:
            return False  # Si es divisible por cualquier número en el rango, no es primo
    return True  # Si no se encuentra divisor, es primo

# Ciclo principal para que el usuario decida continuar
while True:
    # Solicitar al usuario un número entre 10 y 90
    while True:
        try:
            numero = int(input("Introduce un número entre 10 y 90: "))
            if 10 <= numero <= 90:  # Verificar que el número esté dentro del rango
                break
            else:
                print("El número debe estar entre 10 y 90. Intenta de nuevo.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

    # Comprobar si el número es primo
    if es_primo(numero):
        print(f"El número {numero} es primo.")
    else:
        print(f"El número {numero} no es primo.")

    # Preguntar al usuario si desea realizar otra comprobación
    respuesta = input("¿Deseas comprobar otro número? (si/no): ").strip().lower()
    if respuesta != 'si':
        print("Gracias por usar el programa. ¡Hasta luego!")
        break  # Salir del ciclo si la respuesta no es "si"
