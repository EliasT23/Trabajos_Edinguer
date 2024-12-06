# Programa 10/Bloque 2
### Netflix
- En este prograa se utilizan 2 if.
- uno es para saber si el usuario es mayor de edad.
- Y otro para saber si esta pagando la subscripción.
- En caso de no ser mayor de edad no se le permite acceso a netflix
- De igual manera si no lo paga
```python
edad = int(input("Edad "))

if edad >= 18:
    
    peli = int(input("Compraste la pelicula\n 1=si\t 0=no \n"))
    if peli == 1:
        print("Tienes acceso a ver tus cochinadas \U0001F437 ")
    else:
        print("Nececitas tener mas de 18 años para ver peliculas de adultos ")
        
else:
    print("Necesitas tener mas de 18 años para entrar")
