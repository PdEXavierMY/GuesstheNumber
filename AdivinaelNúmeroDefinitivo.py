import random
print("Se va a generar un número aleatorio entero de entre 0 y 99.")
numero = random.randint(0, 99)

def pedir_numero(): 
    while True: 
        entrada = input("Introduzca un número entre 0 y 99: ") 
        try: 
            entrada = int(entrada) 
        except: 
            print("Solo un numero del 0 al 99 es válido")
            pass
        else: 
            if 0 <= entrada <= 99: 
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