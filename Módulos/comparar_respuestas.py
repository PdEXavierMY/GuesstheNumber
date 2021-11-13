SI = ("s", "si", "y", "yes", "1", "Sí", "sí", "SÍ", "SI", "YES", "Y", "S")
VERDADERO = ("v", "verdadero", "t", "true", "1", "Verdadero", "V", "T", "True", "VERDADERO", "TRUE")


def pedir_entrada_si_o_no(invite):
    """Por defecto, toda respuesta no comprendida será NO"""
    try:
        return input(invite).lower() in SI
    except:
        return False

def pedir_entrada_verdadero_o_falso(invite):
    """Por defecto, toda respuesta no comprendida será FALSO"""
    try:
        return input(invite).lower() in VERDADERO
    except:
        return False