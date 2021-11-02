import random
naleatorio = random.randint(0, 100)
nelegido = input(print("Introduce el número generado: "))
while nelegido != naleatorio:
    print("El número elegido no es el correcto")
    if nelegido < naleatorio:
        print("El número generado es menor al introducido")
    else:
        print("El número generado es mayor al introducido")