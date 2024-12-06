# Programa 7/Bloque 1
### Area del circulo
- Este programa utliza el "inport math" para solicitar la función matematica PI.
- Despues pide el radio para calcular su area.
```python
import math 
radio = float(input("Introduce el radio del circulo"))
perimetro = (2 * math.pi * radio)
area = (math.pi*radio**2)
print(f"el perimetro del circulo es :{perimetro}")
print(f"el area del circulo es :{area}")
