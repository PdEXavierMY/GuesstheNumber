from .pedir_números import (pedir_entrada_numero, pedir_entrada_numero_delimitado)


def nivel1():
    minimo = 0
    maximo = 99
    return minimo, maximo

def nivel2():
    minimo = 0
    maximo = 1000
    return minimo, maximo

def nivel3():
    minimo = 0
    maximo = 1000000
    return minimo, maximo

def nivel4():
    minimo = 0
    maximo = 1000000000000
    return minimo, maximo

def elegirnivel():
    print("Hay cuatro niveles de dificultad: 1, 2, 3, 4, aumentando la dificultad del juego cuanto mayor sea el número escogido")
    nivel = pedir_entrada_numero_delimitado("Intoduzca el nivel que quiere jugar", 1, 4)
    return nivel