import math
#Ejercicio 1
def hola_mundo():
    print("Hola mundo")
    
#hola_mundo()

#Ejercicio 2
def es_multiplo(n,m) -> int:

    if (n % m) == 0:
        res = "Es multiplo"
    else:
        res = "No es multiplo"

    return res

# print(es_multiplo(10,2))        

#Ejercicio 3

def es_nombre_largo(nombre) -> str:
    return len(nombre) >= 3 and len(nombre) <= 8

#Ejercicio 5

def devolver_doble_si_par(numero) -> int:
    par = 2
    if numero % par == 0:
        resultado = numero * 2
    else:
        resultado = numero
    return resultado


# print(devolver_doble_si_par(3))

#Ejercicio 6

def pares_entre_numeros() -> int:
    numero = 10
    while numero <= 40:
        if numero % 2 == 0:
            print(numero)
                    
        numero += 1
    
    return

#print(pares_entre_numeros())

def perimetro() -> float:
    res: float = 2*math.pi
    return res

print(perimetro())