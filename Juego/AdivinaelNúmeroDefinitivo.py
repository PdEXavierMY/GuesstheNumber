from Módulos import(pedir_entrada_numero, pedir_entrada_numero_delimitado, pedir_entrada_si_o_no)

def decidir_limites():
    while True:
        minimo = pedir_entrada_numero("¿Cuál es el límite inferior? ")
        maximo = pedir_entrada_numero("¿Cuál es el límite superior? ")
        if maximo > minimo:
            return minimo, maximo

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
    while True:
        victoria, minimo, maximo = jugar_una_vez(numero, minimo, maximo)
        print("Llevas " + str(rondas) + " intentos")
        rondas += 1
        if victoria:
            return

def rondaslimite():
    rondas = 1
    if pedir_entrada_si_o_no("¿Desea tener intentos límite?"):
        rondaslimite = pedir_entrada_numero("¿Cuántos intentos quieres establecer como límite?: ")
        while jugar_una_PARTIDA():
            if rondas == rondaslimite:
                break
            else:
                print("Llevas " + str(rondas) + " intentos.")
                rondas += 1
    else:
        while jugar_una_PARTIDA():
            print("Llevas " + str(rondas) + " intentos.")
            rondas += 1

def jugar():
    minimo, maximo = decidir_limites()
    while True:
        numero = pedir_numero_incognita(minimo, maximo)
        jugar_una_PARTIDA(numero, minimo, maximo)
        rondaslimite()
        if not pedir_entrada_si_o_no("¿Desea jugar una nueva partida?: "):
            print("¡Hasta pronto!")
            return