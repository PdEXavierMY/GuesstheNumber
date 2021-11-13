import sys

def pedir_numero(invitacion):
    while True: 
        entrada = input(invitacion) 
        try: 
            entrada = int(entrada)
        except:
            print("Solo estan autorizados los carácteres [0-9].", file = sys.stderr)
        else: 
            return entrada

def decidir_limites():
    while True:
        minimo = pedir_numero("¿Cuál es el límite inferior? ")
        maximo = pedir_numero("¿Cuál es el límite superior? ")
        if maximo > minimo:
            return minimo, maximo

def pedir_numero_limite(invitacion, minimo, maximo):
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

def pedir_numero_incognita(minimo, maximo):
    return pedir_numero_limite("Introduzca el número a adivinar", minimo, maximo)

def jugar_una_PARTIDA(numero, minimo, maximo):
    rondas = 1
    while True:
        victoria, minimo, maximo = jugar_una_vez(numero, minimo, maximo)
        print("Llevas " + str(rondas) + "intento.")
        rondas += 1
        if victoria:
            return

def jugar():
    minimo, maximo = decidir_limites()
    numero = pedir_numero_incognita(minimo, maximo)
    jugar_una_PARTIDA(numero, minimo, maximo)

jugar()