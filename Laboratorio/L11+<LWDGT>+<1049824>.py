print()
print("Semana No. 11: Ejercicio 1")
print()
N=0
while N<=0:
    N=int(input("Ingrese un número mayor a cero: "))
    if N<=0:
        print("El valor ingresado debe ser mayor a 0")
        print()
#El valor N ha sido leido 
A=0
B=1
C=0
i=2
resultado=" "
resultado=str(A)
if N>1:
    resultado+=(", "+str(B))
    while i<N:
        C=A+B
        resultado+=(", "+str(C))
        A=B
        B=C
        i=i+1
    print(resultado)
else: 
    print(resultado)


print()
print()

print("Semana No. 11: Ejercicio 2")
print()
n2 = int(input("Ingrese un número mayor  cero: "))

if (n2 <= 0 ):
    print("El valor ingresado debe ser mayor a 0")

#A
calculoA= 0
for xA in range (1, n2 + 1):
    calculoA += 1 / xA
print ("El resultado de A es", calculoA)

#B
calculoB = 0
for xB in range(1,n2+1):
            calculoB += 1/(2**xB)
print ("El resultado de B es", calculoB)

#C 
x = int(input("Ingrese un número entero positivo para x: "))
a = int(input("Ingrese un número entero positivo para a: "))
calculoC = 0
for xC in range(1, n2+1):
            calculoC += x**(xC) * a**(n2-xC)
print ("El resultado de C es", calculoC)






