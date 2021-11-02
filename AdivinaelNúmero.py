import random
naleatorio = int(random.randint(0, 100))
nelegido = print(input("Introduce el número que crees que se ha generado: "))
intentos = 1
while nelegido != naleatorio:
    print("El número elegido no es el correcto")
    if nelegido < naleatorio:
        print("El número generado es menor al introducido")
    else:
        print("El número generado es mayor al introducido")
    print("Vuelve a intentarlo")
    intentos += 1
    nelegido = print(input("Introduce el número que crees que se ha generado: "))
if nelegido == naleatorio:
    print("Has acertado!!!")
    print("El número de intentos que has necesitado es " + str(intentos))