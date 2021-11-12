import random
print("Se va a generar un número aleatorio entero de entre 0 y 99.")
numero = random.randint(0, 99)

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