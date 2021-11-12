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
while nelegido != naleatorio:
    print("El número elegido no es el correcto.")
    if nelegido < naleatorio:
        print("El número generado es mayor al introducido.")
    elif nelegido > naleatorio:
        print("El número generado es menor al introducido.")
        print("Vuelve a intentarlo.")
    else:
        print("Has acertado!!!")
        print("El número de intentos que has necesitado es " + str(intentos))
    intentos += 1
    while True:
        nelegido = input("Introduce el número que crees que se ha generado: ")
        try:
            nelegido = int(nelegido)
        except:
            print("Por favor, introduce un número entero del 0 al 99")
        else:
            if 0 <= nelegido <= 99:
                break