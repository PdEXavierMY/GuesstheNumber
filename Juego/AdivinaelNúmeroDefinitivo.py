from Módulos import(ayuda, pedir_entrada_numero, pedir_entrada_numero_delimitado, pedir_entrada_si_o_no, pedir_entrada_numero_delimitado_sinayuda)

def decidir_limites():
    while True:
        minimo = pedir_entrada_numero("¿Cuál es el límite inferior? ")
        maximo = pedir_entrada_numero("¿Cuál es el límite superior? ")
        if maximo > minimo:
            return minimo, maximo

def elegirnivel():
    print("Hay cuatro niveles de dificultad: 1, 2, 3, 4, aumentando la dificultad del juego cuanto mayor sea el número escogido.")
    print("El nivel 1 va del 0 al 100")
    print("El nivel 1 va del 0 al 1000")
    print("El nivel 3 va del 0 al 1000000")
    print("El nivel 4 va del 0 al 1000000000000")
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

def jugar_una_vez_sinayuda(numero, minimo, maximo): 
    intento = pedir_entrada_numero_delimitado_sinayuda("Adivine el número", minimo, maximo)
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

def jugar_una_PARTIDA_sinayuda(numero, minimo, maximo):
    rondas = 1
    if pedir_entrada_si_o_no("¿Desea tener intentos límite? "):
        rondaslimite = pedir_entrada_numero("¿Cuántos intentos quieres establecer como límite?")
        while True:
            if rondaslimite < rondas:
                print("Has alcanzado el número máximo de intentos :( ")
                return
            victoria, minimo, maximo = jugar_una_vez_sinayuda(numero, minimo, maximo)
            print("Llevas " + str(rondas) + " intentos.")
            rondas += 1
            if victoria:
                return
    else:
        while True:
            victoria, minimo, maximo = jugar_una_vez_sinayuda(numero, minimo, maximo)
            print("Llevas " + str(rondas) + " intentos.")
            rondas += 1
            if victoria:
                return

def jugar():
    import random
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
    Boolean = ayuda()
    if Boolean == False:
         while True:
            numero = random.randint(minimo, maximo)
            jugar_una_PARTIDA_sinayuda(numero, minimo, maximo)
            if not pedir_entrada_si_o_no("¿Desea jugar una nueva partida?: "):
                print("¡Hasta pronto!")
                return
    else:
        while True:
            numero = random.randint(minimo, maximo)
            jugar_una_PARTIDA(numero, minimo, maximo)
            if not pedir_entrada_si_o_no("¿Desea jugar una nueva partida?: "):
                print("¡Hasta pronto!")
                return