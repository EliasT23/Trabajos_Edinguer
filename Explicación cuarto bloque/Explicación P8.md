# programa 8/Bloque 4
### While en for
- Este programa aparte de hacer lo que el programa 6
- Pide al usuario si decea repetir el ciclo o terminarlo
- Esto es posible gracias a la función .lower
- Ya que con esta función es posible seleccionar si se decea salir o no
- Y por ultimo usa un "try" para colocar el repetidor de while
```python
def operaciones(num1, num2, digitos):
    for i in range(5):  # El ciclo se ejecutará 5 veces
        suma = num1 + num2
        resta = num1 - num2
        division = round(num1 / num2, digitos) if num2 != 0 else "División por cero no permitida"
        modulo = num1 % num2 if num2 != 0 else "Indefinido"

        print(f"Iteración {i + 1}:")
        print(f"La suma de {num1} y {num2} es: {suma}")
        print(f"La resta de {num1} y {num2} es: {resta}")
        print(f"La división de {num1} y {num2} es: {division}")
        print(f"El módulo de {num1} y {num2} es: {modulo}")
        print("-" * 40)

        # Duplicar los números para la siguiente iteración
        num1 *= 2
        num2 *= 2

# Ciclo principal para continuar pidiendo números o salir
while True:
    # Solicitar los números y los dígitos para la división
    try:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        digitos = int(input("Introduce la cantidad de dígitos decimales para la división: "))
    except ValueError:
        print("Por favor, ingresa valores válidos.")
        continue  # Si hay un error en la entrada, pedir de nuevo los números

    # Llamar a la función de operaciones
    operaciones(num1, num2, digitos)

    # Preguntar al usuario si desea continuar
    respuesta = input("¿Deseas continuar? (si/no): ").strip().lower()
    if respuesta != 'si':
        print("Gracias por usar el programa. ¡Hasta luego!")
        break  # Si la respuesta no es "si", salir del ciclo y terminar el programa
