import random
numero = random.randint(0, 100)

def pedir_numero(): 
    while True: 
        entrada = input("Introduzca un número entre 0 y 99: ") 
        try: 
            entrada = int(entrada) 
        except: 
            pass 
        else: 
            if 9 <= entrada <= 99: 
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