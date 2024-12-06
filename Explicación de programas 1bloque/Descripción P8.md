#Programa 8/Bloque 1
### Calculadora de tiempo
- Solicita al usuario un número entero de días utilizando input()y lo convierte en un número entero con int().
- Despues calcula Cuantas horas, minutos y mesea hay segun el número de dias
```python
dias=int(input("Digite el  numero de dias: "))
horas= (dias * 24)
minutos=(horas * 60)
meses=(dias / 30)

print("El numero de horas es: ",horas)
print("El numero de minutos es : ",minutos)
print("El numero de meses es: ",meses)
