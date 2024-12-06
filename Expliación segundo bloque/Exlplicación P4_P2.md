# Programa 4_P2/Bloque 2
### Programa 4 ( con el bloque ELIF )
- Este programa vemos el bloque Elif.
- Elif simplifica el tener que usar mas de un if
- usando solo elif y no if y else repetidas veces
```python
ing = input("¿Cuáles son tus ingresos?")
ing = float(ing)

if ing <= 1000:
    imp = ing * .05
elif ing > 1000 and ing <= 2500 :
    imp = ing * .08
elif ing > 2500 and ing <= 6000 :
    imp = ing * .08
else:
    imp = ing * .08
    
    
sal_tot = ing - imp  
print("Tu ingresaste:\t"+str(ing)+"\nTus impuestos son:\t"+str(imp)+"\nTu salario séra de:\t"+str(sal_tot))

    
