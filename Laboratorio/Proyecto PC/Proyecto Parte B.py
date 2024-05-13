# Willard Garcia y Ximena Girón Proyecto

nombre = input("¿Cuál es tu nombre?: ")
edad = int(input("¿Cuántos años tienes?: "))
print("Entre estos colores:")
print("rojo")
print("azul")
print("verde")
print("amarillo")
print("naranja")
color_usuario = input("¿Cuál es tu color favorito?: ")
colores = {
    "rojo": "red",
    "azul": "blue",
    "verde": "green",
    "amarillo": "yellow",
    "naranja": "orange",
}

color_programa = colores.get(color_usuario.lower(), "Desconocido")

import turtle

def Paneles(x, y, ancho, alto, texto):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    turtle.color("white")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(ancho)
        turtle.right(90)
        turtle.forward(alto)
        turtle.right(90)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(x + ancho // 2, y - 5)
    turtle.color("black")
    turtle.write(texto, align="center", font=("Arial", 12, "normal"))

def Secuencia_Uno(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    turtle.color("gray")
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(50)
        turtle.right(90)
    turtle.end_fill()

    turtle.goto(x, y + 50)
    turtle.color("red")
    turtle.begin_fill()
    turtle.goto(x + 25, y + 100)
    turtle.goto(x + 50, y + 50)
    turtle.goto(x, y + 50)
    turtle.end_fill()

    turtle.goto(x + 15, y)
    turtle.color("brown")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(20)
        turtle.right(90)
        turtle.forward(30)
        turtle.right(90)
    turtle.end_fill()

    turtle.goto(x + 5, y + 35)
    turtle.color("blue")
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(10)
        turtle.right(90)
    turtle.end_fill()

def Secuencia_Dos(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    # Tronco del árbol
    turtle.color("brown")
    turtle.begin_fill()
    turtle.goto(x + 10, y)
    turtle.goto(x + 10, y + 80)
    turtle.goto(x - 10, y + 80)
    turtle.goto(x - 10, y)
    turtle.end_fill()

    # Hojas del árbol
    turtle.penup()
    turtle.goto(x - 40, y + 80)
    turtle.pendown()
    turtle.color("green")
    turtle.begin_fill()
    turtle.circle(40)
    turtle.end_fill()

    # Más detalles en las hojas
    turtle.penup()
    turtle.goto(x - 20, y + 120)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(x + 20, y + 100)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()

def Secuencia_Tres(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    # Dibujar la pizza
    turtle.color("saddlebrown")
    turtle.begin_fill()
    turtle.circle(100)
    turtle.end_fill()

    num_rebanadas = 8
    angle = 360 / num_rebanadas
    for i in range(num_rebanadas):
        turtle.color("yellow")
        turtle.goto(x, y)
        turtle.begin_fill()
        turtle.setheading(angle / 2 + i * angle)
        turtle.forward(100)
        turtle.setheading(angle + angle / 2 + i * angle)
        turtle.circle(100, angle)
        turtle.end_fill()

    turtle.color("black")
    turtle.width(2)
    turtle.circle(100)

    # Dibujar peperoni
    turtle.penup()
    turtle.goto(x - 80, y + 50)
    turtle.pendown()
    turtle.color("red")
    for _ in range(10):
        turtle.begin_fill()
        turtle.circle(5)
        turtle.end_fill()
        turtle.penup()
        turtle.forward(20)
        turtle.pendown()

def Secuencia_Cuatro(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    # Cuerpo del carro
    turtle.color("blue")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(40)
        turtle.right(90)
    turtle.end_fill()

    # Ventana del carro
    turtle.penup()
    turtle.goto(x + 20, y + 20)
    turtle.pendown()
    turtle.color("white")
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(20)
        turtle.right(90)
    turtle.end_fill()

    # Llantas
    turtle.penup()
    turtle.goto(x - 10, y - 20)
    turtle.pendown()
    turtle.color("black")
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(x + 90, y - 20)
    turtle.pendown()
    turtle.color("black")
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()

def Secuencia_Cinco(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    # Base del hospital
    turtle.color("white")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(150)
        turtle.right(90)
        turtle.forward(200)
        turtle.right(90)
    turtle.end_fill()

    # Parte superior del hospital
    turtle.penup()
    turtle.goto(x + 25, y + 200)
    turtle.pendown()
    turtle.color("red")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(50)
        turtle.right(90)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(x + 75, y + 250)
    turtle.pendown()
    turtle.color("green")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(25)
        turtle.right(90)
    turtle.end_fill()

    # Cruz roja
    turtle.penup()
    turtle.goto(x + 50, y + 100)
    turtle.pendown()
    turtle.color("red")
    turtle.begin_fill()
for _ in range(4):
   turtle.forward(50)
   turtle.right(90)
turtle.end_fill()

# Cruz vertical
turtle.penup()
turtle.goto(x= + 75, y= + 175)
turtle.pendown()

turtle.color("white")
turtle.width(10)
turtle.goto(x= + 75, y= + 25)

# Cruz horizontal
turtle.penup()
turtle.goto(x= + 25, y= + 100)
turtle.pendown()

turtle.width(10)
turtle.goto(x= + 125, y= + 100)

# Techo
turtle.penup()
turtle.goto(x= + 75, y= + 275)
turtle.pendown()
turtle.color("brown")
turtle.begin_fill()
turtle.goto(x= + 125, y= + 250)
turtle.goto(x= + 25, y= + 250)
turtle.goto(x= + 75, y= + 275)
turtle.end_fill()

turtle.speed(0)
ventana = turtle.Screen()
ventana.title("Escena con cinco casas")
ventana.bgcolor("white")

textos_superior = ["Casa de "+str(nombre), "Bosque de la tristeza", "El hambre lo invade", "El Accidente que lo cambió todo", "El Perdón"]
textos_inferior = ["Había una vez un niño que tenía "+str(edad)+" años y se llamaba " +str(nombre)+", que no le hizo caso a sus papás y se escapo de su casa. ",
                  "Al momento de escapar termino perdiéndose en un bosque donde le dio hambre al pasar las horas, lo único que podia pensar era en regresar a su casa para cenar.",
                  "Pasaron horas y empezó a imaginarse una pizza; recapacitó sobre sus acciones y se dio cuenta que si le hubiera hecho caso a sus papás nada de de eso estuviera pasando.",
                  "Cuando encontró el camino de regreso a su casa iba pasando un carro, ya que era de noche no vio a "+str(nombre)+ "cruzar la calle, y rozó al momento de tratar de esquivarlo.",
                  "El niño despertó en el hospital con sus papás al lado, el niño pidió perdón por todo lo que hizo, y diciendo que si les hubiera obedecido todo hubiera salido diferente, desde ese entonces nunca desobedeció a sus papás"]

Paneles(-250, 200, 500, 50, textos_superior[0])
for i in range(5):
   Secuencia_Uno(-200 + i * 100, 0)
Paneles(-250, -150, 500, 100, textos_inferior[0])

def mostrar_secuencia_dos(x, y):
   # Limpiar la ventana actual
   ventana.clear()

   # Dibujar los árboles
   Paneles(-250, 200, 500, 50, textos_superior[1])
   Secuencia_Dos(-150, -100)
   Secuencia_Dos(0, -100)
   Secuencia_Dos(150, -100)
   Paneles(-250, -150, 500, 100, textos_inferior[1])

   # Configurar el evento de clic para mostrar la secuencia tres
   turtle.onscreenclick(mostrar_secuencia_tres)

turtle.onscreenclick(mostrar_secuencia_dos)

def mostrar_secuencia_tres(x, y):
   # Limpiar la ventana actual
   ventana.clear()

   # Dibujar la secuencia tres
   Paneles(-250, 200, 500, 50, textos_superior[2])
   Secuencia_Tres(-150, -100)
   Paneles(-250, -150, 500, 100, textos_inferior[2])
   # Esperar a que se haga clic para salir
   turtle.onscreenclick(mostrar_secuencia_cuatro)

def mostrar_secuencia_cuatro(x, y):
   ventana.clear()
   Paneles(-250, 200, 500, 50, textos_superior[3])
   Secuencia_Cuatro(-150, -100)
   Paneles(-250, -150, 500, 100, textos_inferior[3])
   turtle.onscreenclick(mostrar_secuencia_cinco)

def mostrar_secuencia_cinco(x, y):
   ventana.clear()
   Paneles(-250, 200, 500, 50, textos_superior[4])
   Secuencia_Cinco(-150, -100)
   Paneles(-250, -150, 500, 100, textos_inferior[4])
   turtle.exitonclick()

ventana.mainloop()