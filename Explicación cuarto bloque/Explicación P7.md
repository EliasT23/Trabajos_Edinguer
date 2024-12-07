# Programa 7/Bloque 4
### Rango en for
- Replica del programa 6
- Pero este programa usa un rango de numeros hasta 5
- Y al llegar a ese numero termina el ciclo
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

# Llamar a la función con valores iniciales
operaciones(10, 5, 2)
