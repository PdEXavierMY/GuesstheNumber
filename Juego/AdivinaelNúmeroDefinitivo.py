from Módulos import(pedir_entrada_numero, pedir_entrada_numero_delimitado, pedir_entrada_si_o_no)

def decidir_limites():
    while True:
        minimo = pedir_entrada_numero("¿Cuál es el límite inferior? ")
        maximo = pedir_entrada_numero("¿Cuál es el límite superior? ")
        if maximo > minimo:
            return minimo, maximo

def elegirnivel():
    print("Hay cuatro niveles de dificultad: 1, 2, 3, 4, aumentando la dificultad del juego cuanto mayor sea el número escogido.")
    nivel = pedir_entrada_numero_delimitado("Intoduzca el nivel que quiere jugar", 1, 4)
    return nivel

def jugar_una_vez(numero, minimo, maximo): 
    intento = pedir_entrada_numero_delimitado("Adivine el número", minimo, maximo)
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
    return pedir_entrada_numero_delimitado("Introduzca el número a adivinar", minimo, maximo)

def jugar_una_PARTIDA(numero, minimo, maximo):
    rondas = 1
    if pedir_entrada_si_o_no("¿Desea tener intentos límite? "):
        rondaslimite = pedir_entrada_numero("¿Cuántos intentos quieres establecer como límite?")
        while True:
            if rondaslimite < rondas:
                print("Has alcanzado el número máximo de intentos :( ")
                return
            victoria, minimo, maximo = jugar_una_vez(numero, minimo, maximo)
            print("Llevas " + str(rondas) + " intentos.")
            rondas += 1
            if victoria:
                return
    else:
        while True:
            victoria, minimo, maximo = jugar_una_vez(numero, minimo, maximo)
            print("Llevas " + str(rondas) + " intentos.")
            rondas += 1
            if victoria:
                return

def jugar():
    import random
    from Módulos.pedir_números import(ayuda)
    n = elegirnivel()
    if n == 1:
        minimo = 0
        maximo = 100
    elif n == 2:
        minimo = 0
        maximo = 1000
    elif n == 3:
        minimo = 0
        maximo = 1000000
    else:
        minimo = 0
        maximo = 1000000000000
    ayuda()
    while True:
        numero = random.randint(minimo, maximo)
        jugar_una_PARTIDA(numero, minimo, maximo)
        if not pedir_entrada_si_o_no("¿Desea jugar una nueva partida?: "):
            print("¡Hasta pronto!")
            return