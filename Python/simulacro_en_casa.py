def ultima_aparicion(lista_1:list, elemento:int) -> int:
    
    res:int = -1

    for numero in range(len(lista_1)):
        if lista_1[numero] == elemento:
            res = numero
    return res

def elementos_exclusivos(lista_1:list,lista_2:list) -> list:
    lista_elementos_exclusivos:list = []

    for numero in lista_1:
        if numero not in lista_2 and numero not in lista_elementos_exclusivos:
            lista_elementos_exclusivos.append(numero)

    for numero in lista_2:
        if numero not in lista_1 and numero not in lista_elementos_exclusivos:
            lista_elementos_exclusivos.append(numero)
    
    return lista_elementos_exclusivos

def contar_traducciones_iguales(ingles:dict,aleman:dict) -> int:
    
    traducciones_iguales:int = 0

    for palabra_ingles, traduccion_ingles in ingles.items():
        for palabra_aleman, traduccion_aleman in aleman.items():

            if palabra_ingles == palabra_aleman and traduccion_ingles == traduccion_aleman:
                traducciones_iguales += 1

    return traducciones_iguales

def convertir_a_diccionario(lista:list) -> dict:
    
    cantidad_por_numero:dict = {}

    for elemento in lista:
        if elemento in cantidad_por_numero:
            cantidad_por_numero[elemento] += 1
        else:
            cantidad_por_numero[elemento] = 1
            
    return cantidad_por_numero

