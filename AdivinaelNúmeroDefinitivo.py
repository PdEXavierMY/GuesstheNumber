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

def jugar():
    minimo, maximo = decidir_limites()
    numero = pedir_numero_incognita(minimo, maximo)
    jugar_una_PARTIDA(numero, minimo, maximo)

if __name__ == '__main__':
    print("Se ha ejecutado el módulo")
    jugar()
else:
    print("Se ha importado el módulo")