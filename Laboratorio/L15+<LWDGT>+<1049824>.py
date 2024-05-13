print()
import math
def menu():
    print("Elija una opcion: ","a. Área de triángulo", "b. Área de cuadrado", "c. Área de rectángulo", "d. Área de círculo", sep = "\n" )
    opcion=input()
    return opcion 
def ObtenerAreaTriangulo(base,altura):
    area=(base*altura)/2
    return area
def ObtenerAreaCuadrado(lado):
    area2=lado**2
    return area2
def ObtenerAreaRectangulo(base,altura):
    area3=base*altura
    return area3
def ObtenerAreaCirculo(radio): 
    area4= math.pi*radio
    return area4
print("Semana No. 15: Ejercicio 1")

match menu():
    case "a": 
        print("El área del triángulo es: ", ObtenerAreaTriangulo(float(input("Ingrese la base del triángulo: ")), float(input("Ingrese la altura del triángulo"))))
    case "b": 
        print("El área del cuadrado es: ", ObtenerAreaCuadrado(float(input("Ingrese el lado del cuadrado: "))))
    case "c": 
        print("El área del rectángulo es: ", ObtenerAreaRectangulo(float(input("Ingrese la base del Rectángulo: ")), float(input("Ingrese la altura del Rectángulo"))))
    case "d": 
        print("El área del Círculo es: ", round(ObtenerAreaCirculo(float(input("Ingrese el radio del circulo: "))),2))
    


print()
print("Semana No. 15: Ejercicio 2")

x = 0
y = 0

def menu():
    print("Seleccione una opción:", "a. Sube", "b. Baja", "c. Izquierda", "d. Derecha", "e. Salir", sep = "\n")
    opcion = input("Ingrese una opción: ")
    return opcion

def moverHaciaArriba():
    global y
    y += 1

def moverHaciaAbajo():
    global y
    y -= 1

def moverHaciaLaDerecha():
    global x
    x += 1

def moverHaciaLaIzquierda():
    global x
    x -= 1

while True:
    opcion = menu()
    match opcion:
        case "a":
            moverHaciaArriba()
        case "b":
            moverHaciaAbajo()
        case "c":
            moverHaciaLaIzquierda()
        case "d":
            moverHaciaLaDerecha()
        case "e":
            print("Coordenadas finales del personaje: " + str(x) + "," + str(y))
            break
        case _:
            print("Opción inválida. Intente nuevamente.")