# Programa 2/Bloque 3
### Comparacion de números.
- El usuario ingresara 2 números.
- Luego se hara una comparacion para saber cual es mayor.
```python
n1 = int(input("Ingrese el numero 1 :"))
n2 = int(input("Ingrese el numero 2 :"))

if n1 > n2:
    print("El numero "+str(n1)+" es mayor al numero "+str(n2))
elif n1==n2:
    print("son iguales los dos numeros")
else:
    print("El numero "+str(n1)+" es menor al numero "+str(n2))
