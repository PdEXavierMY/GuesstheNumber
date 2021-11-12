import random
print("Se va a generar un número aleatorio entero de entre 0 y 99.")
aleatorio = random.randint(0, 99)

def pedir_numero(invitacion, minimo, maximo):
    invitacion += " Entre " + str(minimo) + " y " + str(maximo) + " : "
    while True: 
        entrada = input(invitacion) 
        try: 
            entrada = int(entrada)
        except:
            pass
        else: 
            if minimo <= entrada <= maximo: 
                break 
    return entrada

minimo = MIN
maximo = MAX
print("Intente adivinar el número") 
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