print("Semana 12: Ejercicio 1")
print("a. Sumatoria")
print("b. Factorial")
print("c. Tablas de Multiplicar")
print("d. Número perfecto")

opcion=input("Elija una de las opciones a calcular: ")
match opcion: 
    case "a":
        N=0
        while N<=0:
        
            N=int(input("Ingrese un número entero positivo"))
            if N<=0:
                print("El número ingresado debe ser mayor a cero")
        sumatoria=0
        for cont in range (1, N+1):
            sumatoria+=cont 
        print("La sumatoria es: ", sumatoria)
    
    case "b":
        N=0
        while N<=0:
        
            N=int(input("Ingrese un número entero positivo"))
            if N<=0:
                print("El número ingresado debe ser mayor a cero")
        factorial=1
        for cont in range (1, N+1):
            factorial*=cont 
        print("La factorial es: ", factorial)
    
    case "c": 
        for i in range (1,11):
            for j in range (1,11):
                print(i*j, "\t", end=" ")
            print()

    case "d":
        N=0 
        while N<=0:
            N=int(input("Ingrese un número entero positivo: "))
            if N<=0:
                print("El número ingresado debe ser mayor que 0.")
        sumatoria=0

        for factor in range (1,N):
            if N%factor ==0:
                sumatoria +=factor 
        if sumatoria==N:
            print("El número es perfecto")
        else: 
            print("El numeo no es perfecto")

    case _:
        print("Ingrese una opción válida")
        