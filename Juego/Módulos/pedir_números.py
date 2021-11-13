import sys

from Juego.Módulos.comparar_respuestas import pedir_entrada_verdadero_o_falso

MIN=0
MAX=100


def pedir_entrada_numero(invitacion):
    while True:
        print(invitacion, end = ": ")
        entrada = input()
        try:
            entrada = int(entrada)
        except:
            print("Solo los caracteres [0-9] están autorizados.", file = sys.stderr)
        else:
            return entrada

def pedir_entrada_numero_delimitado(invitacion, minimo=MIN, maximo=MAX):
    ayuda = pedir_entrada_verdadero_o_falso("¿Quiere ir actualizando el número mínimo y máximo entre el que se encuentra el número generado? (Es decir, recibir una ayuda extra)")
    if ayuda == True:
        while True:
            entrada = pedir_entrada_numero(invitacion)
            if minimo <= entrada <= maximo:
                return entrada
    else:
        while True:
            invitacion = "{} entre {} y {} incluidos".format(invitacion, minimo, maximo)
            entrada = pedir_entrada_numero(invitacion)
            if minimo <= entrada <= maximo:
                return entrada