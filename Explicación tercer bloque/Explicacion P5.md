# Programa 5/Bloque 3
### Calificaciónes
- Este programa vemos el bloque Elif.
- Este es usado para mostrar que tan bueno es tu promedio
```python
prom = int(input("Ingresa tu promedio de el 10 al 100: \n\t"))

if prom <= 70:
    print("Su promedio no es suficiente \U")
    
elif prom > 70 and prom <=79:
    print("Su promedio apenas es suficiente \U")
    
elif prom > 79 and prom <=89:
    print("Su promedio es bueno \U")
    
elif prom > 89 and prom <=100:
    print("Su promedio es exelente \U")
    
else:
    print("Promedio no valido")
    
