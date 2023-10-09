#PRIMERA PARTE
#EJERCICIO 1

#1.1

def pertenece(lista: list, e: int) -> bool:

    pertenecen:bool = False

    for elemento in lista:
        if lista[elemento] == e:
            pertenecen = True
    return pertenecen

#1.2

def divideATodos(lista: list, e:int) -> bool:

    divide:bool = True
    for elemento in lista:
        if elemento  % e != 0:
            divide = False
    return divide

#1.3

def sumaTotal(lista:list)-> int:
    sumador: int = 0

    for elemento in lista:
        sumador += elemento 
    return sumador

#1.4

def ordenados(lista:list) -> bool:
    orden: bool = True

    for i in range(len(lista) -1):
        if lista[i] >= lista[i+1]:
            orden = False
    return orden

#1.5

def longitudes(lista:list) -> bool:
    hay_palabra_larga: bool

    for palabra in lista:
        if len(palabra ) > 7:
            hay_palabra_larga = True
    return hay_palabra_larga

#1.6

def palindromo(palabra: str) -> bool:
    return palabra == palabra [::-1]

#1.7
def contrasenia(contra:str) -> str:

    longitud = len(contra) > 8
    hay_minuscula =  any(caracter.islower() for caracter in contra)
    hay_mayuscula = any(caracter.isupper() for caracter in contra)
    hay_numero = any(caracter.isdigit() for caracter in contra)
    validador = ""

    if longitud  and hay_minuscula and hay_mayuscula  and hay_numero:
        validador = "VERDE"
    elif len(contra) < 5:
        validador = "ROJA"
    else:
        validador = "AMARILLA"
    return validador

#1.8

def movimientos_bancarios(movimientos: list[(str,int)]) -> int:
    saldo:int = 0

    for transaccion, total in movimientos:
        if transaccion.lower() == 'i':
            saldo += total
        else:
            saldo -= total
    return saldo

#1.9

def tiene_vocal_distinta(palabra:str) -> bool:
    vocales:str = "aeiou"
    distintas_vocales:set = set()

    for caracter in palabra.lower():
        if caracter in vocales:
            distintas_vocales.add(caracter)

    return len(distintas_vocales) >= 3
        

