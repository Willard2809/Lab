
print("Mediciones de los estudiantes de la URL")
nombre=input("Ingrese su nombre: ")
carné=int(input("Ingrese su número de carné: "))
print("Nombre: ",nombre,"No. Carné: ", carné)
print()

medida=int(input("ingrese un valor en metros: "))
milla=(medida/1000)/(1.69)
kilometro=medida/1000
pies=medida*3.28
pulgadas=(medida*3.28)*12
yardas=medida/0.914
metros=medida
print(medida,"metros =",milla,"mi")
print(medida,"metros =",kilometro,"Km")
print(medida,"metros =",pies,"ft")
print(medida,"metros =",pulgadas,"in")
print(medida,"metros =",yardas,"yd")
print(medida,"metros =",metros,"m")
print()