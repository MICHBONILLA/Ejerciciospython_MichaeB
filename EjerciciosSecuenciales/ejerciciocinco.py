#Se declara la variable valorcompra,Se declara la variable valordescuen, Se declara la variable descuento restando la variable valorcompra menos la variable valordescuen y finalmente se muestra el resultado mediante print concatenando la variable valorcompra , valordescuen y descuento

# Se declara la variable valorcompra
valorcompra= int(input(" ingrese el valor de la compra"))
# Se declara la variable valordescuen
valordescuen= int(input(" ingrese el valor del descuento"))
# Se declara la variable descuento restando la variable valorcompra menos la variable valordescuen
descuento=  valorcompra - valordescuen
# se muestra el resultado mediante print concatenando la variable valorcompra , valordescuen y descuento
print (" La compra fue de : ", valorcompra, " con un descuento de:", valordescuen, " y el valor final al pagar es de:", descuento)