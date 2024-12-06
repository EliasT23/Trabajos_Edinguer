#Programa 9/Bloque 2
### Articulos en venta
- Primero se pide al usuario que ingrese la cantidad de articulos.
- Si el número de articulos supera las 3 unidades cada articulo tendra un valor de $30.
- De lo contrario tendra un valor de $45.
- Por ultimo se da el precio total por los articulos comprados.
- En este programa se utiliza un conversor de alfanumerico a entero que es lo siguiente " num_articulos = int(input) "
```python
num_articulos = int(input("Coloque el numero de articulos que decee comprar: "))

if num_articulos > 3:
    precio= num_articulos * 30
    print("Muy bien usted compro:\t",num_articulos,"\nAl costo de $30 por articulo entonces usted pagara: \t"+str(precio))
else:
    precio= num_articulos * 45
    print("Muy bien usted compro:\t",num_articulos,"\nAl costo de $30 por articulo entonces usted pagara: \t"+str(precio))
