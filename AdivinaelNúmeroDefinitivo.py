import random
print("Se va a generar un número aleatorio entero de entre 0 y 99.")
numero = random.randint(0, 99)

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

print("Intente adivinar el número") 
while True: 
    intento = pedir_numero() 
    if intento < numero: 
        print("Demasiado pequeño") 
    elif intento > numero: 
        print("Demasiado grande") 
    else: 
        print ("¡Ha ganado!")
        break