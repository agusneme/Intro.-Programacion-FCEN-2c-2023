#EJERCICIO 1
def ultima_aparicion(s: list, e:int) -> int:
    
    ultima_aparicion = s[::-1].index(e)

    if e in s:
        return len(s) - ultima_aparicion - 1

s = [-1, 4, 0, 4, 100, 0, 100, 0, -1, -1]
e = 0
print(ultima_aparicion(s,e))

#EJERCICIO 2
def elementos_exclusivos(lista_1: list, lista_2: list) -> list:
    elementos_exclusivos:list = []

    for elemento in lista_1: 
        if (elemento not in lista_2) and (elemento not in elementos_exclusivos): 
            elementos_exclusivos.append(elemento)

    for elemento in lista_2:
        if (elemento not in lista_1 )and (elemento not in elementos_exclusivos):
            elementos_exclusivos.append(elemento)

    return elementos_exclusivos

#EJERCICIO 3
def contar_traducciones_iguales(ingles: dict, aleman: dict) -> int:
    
    trad_iguales:int= 0

    for palabra_ingles,traduccion_ingles in ingles.items():
        for palabra_aleman, traduccion_aleman in aleman.items():
            if palabra_ingles == palabra_aleman and traduccion_ingles == traduccion_aleman:
                trad_iguales += 1
    
    return trad_iguales


#EJERCICIO 4
def convertir_a_diccionario(lista: list) -> dict:
    cant_apariciones:dict = {}
    
    for elemento in lista:
        if elemento in cant_apariciones:
            cant_apariciones[elemento] += 1
        else:
            cant_apariciones[elemento] = 1
    return cant_apariciones

lista_1 = [-1, 4, 0, 4, 3, 0, 100, 0, -1, -1]
lista_2 = [0, 100, 5, 0, 100, -1, 5]
print(elementos_exclusivos(lista_1,lista_2))

aleman = {"Mano": "Hand", "Pie": "Fuss", "Dedo": "Finger", "Cara": "Gesicht"}
ingles = {"Pie": "Foot", "Dedo": "Finger", "Mano": "Hand"}
print(contar_traducciones_iguales(ingles,aleman))

lista = [-1, 0, 4, 100, 100, -1, -1] 
print(convertir_a_diccionario(lista))

