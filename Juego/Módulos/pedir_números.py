import sys
from .comparar_respuestas import pedir_entrada_verdadero_o_falso

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

def ayuda():
    ayudas = pedir_entrada_verdadero_o_falso("¿Quieres recibir una ayuda extra durante el juego?(Se te irá actualizando el número mínimo y máximo entre el que está el número generado de entre los que vayas fallando)")
    return ayudas

def pedir_entrada_numero_delimitado(invitacion, minimo=MIN, maximo=MAX):
    if ayuda() == True:
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