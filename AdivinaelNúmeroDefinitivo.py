import sys
MIN = 0
MAX = 99

def pedir_numero(invitacion):
    while True: 
        entrada = input(invitacion) 
        try: 
            entrada = int(entrada)
        except:
            print("Solo estan autorizados los carácteres [0-9].", file = sys.stderr)
        else: 
            return entrada

def pedir_numero_limite(invitacion, minimo=MAX, maximo=MAX):
    while True:
        invitacion = "{} entre {} y {} incluidos".format(invitacion, minimo, maximo)

numero = pedir_numero("Introduzca el número a adivinar")
minimo = MIN
maximo = MAX

while True: 
    intento = pedir_numero("Adivine el número", minimo, maximo) 
    if intento < numero: 
        print("Demasiado pequeño")
        minimo = intento + 1
    elif intento > numero: 
        print("Demasiado grande") 
        maximo = intento - 1
    else: 
        print ("¡Ha ganado!")
        break