import random
print("Se va a generar un número aleatorio entero de entre 0 y 99.")
naleatorio = random.randint(0, 99)
def pedir_numero():
    while True:
        numero = input("Introduce el número que crees que se ha generado: ")
        try:
            numero = int(nelegido)
        except:
            print("Por favor, introduce un número entero del 0 al 99")
        else:
            if 0 <= numero <= 99:
                break
    return numero

intentos = 1
while True:
    intento = pedir_numero()
    intentos += 1
    if numero < naleatorio:
        print("El número introducido no es el correcto")
        print("El número generado es mayor al introducido.")
        print("Vuelve a intentarlo.")
    elif numero > naleatorio:
        print("El número introducido no es el correcto")
        print("El número generado es menor al introducido.")
        print("Vuelve a intentarlo.")
    else:
        print("Has acertado!!!")
        print("El número de intentos que has necesitado es " + str(intentos))