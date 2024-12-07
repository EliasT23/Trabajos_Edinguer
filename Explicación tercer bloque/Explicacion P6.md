# Programa 6/Bloque 3
### Números menores a 50
- En este programa vemos el ciclo for
- Este se ejecutara buscando entre la tabla numeros que esten dentro del rango que en este caso sera 50
- por ultimo mostrara estos números en pantalla
```python
numeros=[10,50,25,13,10,28,100,500,29,29]
menor_50=[]
for numero in numeros:
    if numero < 50:
        menor_50.append(numero)
print("La liste original es: ",numeros,"\nLa nueva lista es: ",menor_50)

