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
        

#SEGUNDA PARTE
#EJERCICIO 2

#2.1

def cambiador_pares(lista:list) -> list:

    for i in range(0,len(lista),2):
        lista[i] = 0
    return lista

#2.2

def cambiador_pares_no_modificando_lista(lista:list) -> list:
    nueva_lista:list = lista.copy()

    for i in range(0,len(nueva_lista),2):
        nueva_lista[i] = 0
    return nueva_lista

#2.3
def palabra_sin_vocales(palabra:str) ->str:

    vocales:str = 'aeiou'
    palabra_sin_vocales:str = ''
    for caracter in palabra:
        if caracter not in vocales:
            palabra_sin_vocales += palabra_sin_vocales

    return palabra_sin_vocales

#2.4

def reemplaza_vocales(secuencia:str) -> str:

    vocales:str = 'aeiou'
    res = []

    for caracter in secuencia:
        if caracter in vocales:
            res.append(' ')
        else:
            res.append(caracter)
    
    return ''.join(res)

#2.5

def darVueltaStr(palabra:str) -> str:
    return palabra[::-1]

#2.6

#EJERCICIO 3

def aprobado(notas:list) -> int:

    aprobacion:int = 0

    promedio = sum(notas)/len(notas)

    for nota in notas:
        if nota < 4 or promedio < 4:
            aprobacion = 3
            break
        elif nota >= 4 and (promedio >= 4 and promedio < 7):
            aprobacion = 2
    return aprobacion

#EJERCICIO 4

#4.1

def estudiantes():
    lista_estudiantes = []

    while True:

        nombres:str = input("Ingrese el nombre del estudiante: ")
        if nombres.lower() == 'listo':
            break

        lista_estudiantes.append(nombres)

    return lista_estudiantes


#4.2

def monedero_electronico():    
    historial_operaciones = []

    while True:
        operacion = input("Que operacion desea realizar? Escriba 'C' para cargar credito, 'D' para descontar creditos o 'X' para terminar el programa. ")

        if operacion.upper() == 'X':
            break

        elif operacion.upper() == 'C':
            transaccion_carga = int(input("Cuantos creditos desea cargar?: "))
            historial_operaciones.append(('C', transaccion_carga))

        elif operacion.upper() == 'D':
            transaccion_descontar = int(input("Cuantos creditos desea descontar?: "))
            historial_operaciones.append(('D', transaccion_descontar))
        

    return historial_operaciones

print(monedero_electronico())