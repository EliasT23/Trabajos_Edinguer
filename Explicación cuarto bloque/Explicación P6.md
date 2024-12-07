# Programa 6/Bloque 4
### Este programa pide dos números para ejecutar operaciones 
- Pide al usuario 2 numeros para despues duplicar su valor 
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
