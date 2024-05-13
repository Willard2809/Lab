# Definir el tamaño del tablero
ttablero = 8
tablero = [['' for _ in range(ttablero)] for _ in range(ttablero)]

# Símbolos Unicode para las piezas
PEON_BLANCO = '♙'
CABALLO_BLANCO = '♘'
ALFIL_BLANCO = '♗'
TORRE_BLANCO = '♖'
REINA_BLANCO = '♕'
REY_BLANCO = '♔'
PEON_NEGRO = '♟'
CABALLO_NEGRO = '♞'
ALFIL_NEGRO = '♝'
TORRE_NEGRO = '♜'
REINA_NEGRO = '♛'
REY_NEGRO = '♚'

# Colores para los espacios blancos y negros
BLANCO = '\033[107m'
NEGRO = '\033[40m'
RESET = '\033[0m'

# Función para validar la posición
def posicion_valida(fila, columna):
    return 0 <= fila < ttablero and 0 <= columna < ttablero

# Función para agregar piezas
def agregar_piezas():
    cantidad_piezas = int(input("Ingresa la cantidad de piezas a agregar: "))
    for _ in range(cantidad_piezas):
        tipo_pieza = input("Ingresa el tipo de pieza (peon, caballo, alfil, torre, reina, rey): ").lower()
        color_pieza = input("Ingresa el color (blanco o negro): ").lower()
        posicion = input("Ingresa la posición (ej. a1, e4, f8): ").lower()
        fila = ttablero - int(posicion[1])
        columna = ord(posicion[0]) - ord('a')
        if posicion_valida(fila, columna) and tablero[fila][columna] == '':
            if color_pieza == 'blanco':
                if tipo_pieza == 'peon':
                    tablero[fila][columna] = PEON_BLANCO
                elif tipo_pieza == 'caballo':
                    tablero[fila][columna] = CABALLO_BLANCO
                elif tipo_pieza == 'alfil':
                    tablero[fila][columna] = ALFIL_BLANCO
                elif tipo_pieza == 'torre':
                    tablero[fila][columna] = TORRE_BLANCO
                elif tipo_pieza == 'reina':
                    tablero[fila][columna] = REINA_BLANCO
                elif tipo_pieza == 'rey':
                    tablero[fila][columna] = REY_BLANCO
            else:
                if tipo_pieza == 'peon':
                    tablero[fila][columna] = PEON_NEGRO
                elif tipo_pieza == 'caballo':
                    tablero[fila][columna] = CABALLO_NEGRO
                elif tipo_pieza == 'alfil':
                    tablero[fila][columna] = ALFIL_NEGRO
                elif tipo_pieza == 'torre':
                    tablero[fila][columna] = TORRE_NEGRO
                elif tipo_pieza == 'reina':
                    tablero[fila][columna] = REINA_NEGRO
                elif tipo_pieza == 'rey':
                    tablero[fila][columna] = REY_NEGRO
        else:
            print("Posición inválida o ya ocupada. Intenta de nuevo.")

# Función para agregar el caballo
def agregar_caballo():
    posicion = input("Ingresa la posición del caballo (ej. a1, e4, f8): ").lower()
    fila = ttablero - int(posicion[1])
    columna = ord(posicion[0]) - ord('a')
    if posicion_valida(fila, columna) and tablero[fila][columna] == '':
        tablero[fila][columna] = CABALLO_NEGRO
    else:
        print("Posición inválida o ya ocupada. Intenta de nuevo.")

# Función para obtener los movimientos válidos del caballo
def obtener_movimientos_validos(fila, columna):
    movimientos = []
    for cambio_fila, cambio_columna in [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]:
        nueva_fila, nueva_columna = fila + cambio_fila, columna + cambio_columna
        if posicion_valida(nueva_fila, nueva_columna):
            pieza = tablero[nueva_fila][nueva_columna]
            if pieza == '':
                movimientos.append((chr(nueva_columna + ord('a')) + str(ttablero - nueva_fila), 'casilla vacía'))
            else:
                movimientos.append((chr(nueva_columna + ord('a')) + str(ttablero - nueva_fila), pieza))
    return movimientos

# Función para mostrar los movimientos válidos
def mostrar_movimientos_validos():
    for fila in range(ttablero):
        for columna in range(ttablero):
            if tablero[fila][columna] == CABALLO_NEGRO:
                movimientos = obtener_movimientos_validos(fila, columna)
                if movimientos:
                    print(f"Movimientos válidos para el caballo en {chr(columna + ord('a'))}{ttablero - fila}:")
                    for movimiento, info in movimientos:
                        print(f"  {movimiento}: {info}")
                else:
                    print(f"No hay movimientos válidos para el caballo en {chr(columna + ord('a'))}{ttablero - fila}.")

# Función para dibujar el tablero
def dibujar_tablero(fila, columna):
    if (fila + columna) % 2 == 0:
        return NEGRO + '   ' + RESET
    else:
        return BLANCO + '   ' + RESET

# Función para imprimir el tablero
def imprimir_tablero():
    print("   " + " ".join([chr(i + ord('a')) for i in range(ttablero)]))
    for fila in range(ttablero):
        print(f"{ttablero - fila} ", end='')
        for columna in range(ttablero):
            pieza = tablero[fila][columna]
            if pieza:
                print(dibujar_tablero(fila, columna) + pieza, end='')
            else:
                print(dibujar_tablero(fila, columna), end='')
        print()

# Función principal
def main():
    agregar_piezas()
    agregar_caballo()
    mostrar_movimientos_validos()
    print("\nTablero:")
    imprimir_tablero()

# Ejecutar el programa
main()