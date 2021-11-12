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
        invitacion = "{} entre {} y {} incluidos ".format(invitacion, minimo, maximo)
        entrada = pedir_numero(invitacion) 
        if minimo <= entrada <= maximo: 
            return entrada

def jugar_una_vez(numero, minimo, maximo): 
    intento = pedir_numero_limite("Adivine el número", minimo, maximo) 
    if intento < numero: 
        print("Demasiado pequeño") 
        minimo = intento + 1 
        victoria = False 
    elif intento > numero: 
        print("Demasiado grande") 
        maximo = intento - 1 
        victoria = False 
    else: 
        print("¡Ha ganado!") 
        victoria = True 
        minimo = maximo = intento 
    return victoria, minimo, maximo

minimo = maximo = 0
while True:
    minimo = pedir_numero("Seleccione el mínimo: ") 
    maximo = pedir_numero("Seleccione el máximo: ") 
    if maximo > minimo: 
        break
numero = pedir_numero_limite("Introduzca el número a adivinar", minimo, maximo) 

while True: 
    victoria, minimo, maximo = jugar_una_vez(numero, minimo, maximo)  
    if victoria: 
        break