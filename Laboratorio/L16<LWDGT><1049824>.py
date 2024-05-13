print()
import random 
print("Semana No. 16: Ejercicio 1")

a=[]
for i in range (10):
    r=random.randint(1,100) 
    a.append(r)

promedio=0
for num in a:
    promedio += num
promedio=promedio/len(a)

print(a)
print("La cantidad de elementos es: ",len(a))
print("El promedio es: ", promedio)

sumap=0
sumai=0
for i in range (len(a)):
    if i%2==0:
       sumap+=a[i]
    else:
        sumai+=a[i]
print("La suma par es: ", sumap)
print("La suma impar es: ", sumai)
print()

print("Semana No. 16: Ejercicio 2")

filas=int(input("Ingrese la cantidad de filas: "))
columnas=int(input("Ingrese la cantidad de columnas: "))
b=[[]]
for i in range(filas):
   fila = []
   for j in range(columnas):
       fila.append(random.randint(0, 1001))
   b.append(fila)

pares = 0
impares = 0
mayor = 0
menor = 1001

for fila in b:
   for numero in fila:
       if numero % 2 == 0:
           pares += 1
       else:
           impares += 1
       if numero > mayor:
           mayor = numero
       if numero < menor:
           menor = numero

print(b)
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
print("Número mayor:", mayor)
print("Número menor:", menor)
