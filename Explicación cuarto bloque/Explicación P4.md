# Programa 4/Bloque 4
### Definicion de Funcion
- Agrupa un conjunto de instrucciones bajo un mismo nombre
- para que las instrucciones puedan ser ejecutadas de manera repetida sin necesidad de reescribir el codigo
```python
def es_primo(numero):
    if numero < 2:
        return False
    for i in range (2, int (numero ** 0.5)+1):
        if numero % i == 0:
            return False 
    return True
    
"""Aqui se le pedira el número del 2 al 99 a el Usuario"""
numero=int(input("ingresa un número entre 10 y 99 \t: "))
    
    
if 10 <= numero <=99:
    if es_primo(numero):
            print(f"El número {numero} es primo.")
    else:
            print(f"El número {numero} no es primo.")
else:
        print("El número no esta en el rango")
