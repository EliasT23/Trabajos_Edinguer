num_articulos = int(input("Coloque el numero de articulos que decee comprar: "))

if num_articulos > 3:
    precio= num_articulos * 30
    print("Muy bien usted compro:\t",num_articulos,"\nAl costo de $30 por articulo entonces usted pagara: \t"+str(precio))
else:
    precio= num_articulos * 45
    print("Muy bien usted compro:\t",num_articulos,"\nAl costo de $30 por articulo entonces usted pagara: \t"+str(precio))