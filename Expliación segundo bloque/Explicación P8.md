# Programa 8/Bloque 2
### Calificaciones 
- El usuario ingresa sus calificaciones.
- Estas se promedian y generan el promedio.
- Despues con la condicionante verificamos si aprueba con ese promedio.
- si es asi enviara un mensaje aprobatorio.
- si no, se enviara un mensaje mencionando que ha reprobado.
```python
cal1= float(input("Cual es tu calificacion de modulo 1? "))
cal2= float(input("Cual es tu calificacion de modulo 2? "))
cal3= float(input("Cual es tu calificacion de modulo 3? "))
cal4= float(input("Cual es tu calificacion de modulo 4? "))
cal5= float(input("Cual es tu calificacion de modulo 5? "))

calf= (cal1+cal2+cal3+cal4+cal5)/5
print("Tu promedio fue de: ",calf)

if calf>=70:
    print("pasaste prro\n")
else:
    print("Tu calificacion no es aprobatoria")
