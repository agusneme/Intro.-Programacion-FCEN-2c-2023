import math
#EJERCICIO 1
#Ejercicio 1.1

def hola_mundo():
    print("Hola Mundo")

#Ejercicio 1.3
def raizde2():

    return round(math.sqrt(2),4)

#Ejercicio 1.4
def factorial(numero:int):
    
    return factorial(numero -1)

#Ejercicio 1.5
def perimetro() -> float:
    res: float = 2*math.pi
    return res

#EJERCICIO 2
#Ejercicio 2.1

def imprimir_saludo(nombre:str) -> str:
    return f"Hola {nombre}"

#Ejercicio 2.2

def raiz_cuadrada_de(numero:int) -> int:
    return math.sqrt(numero)

#Ejercicio 2.3

def farenheit_a_celsius(temp:int) -> int:
    conversor = (temp - 32 * 5) / 9
    return conversor

#Ejercicio 2.4

def imprimir_dos_veces(estribillo:str) -> str:
    return estribillo * 2
#print(imprimir_dos_veces("Hola como estas \n"))

#Ejercicio 2.5

def es_multiplo(n:int,m:int) -> bool:
    return  n % m == 0

#Ejercicio 2.6

def es_par(numero:int) -> bool:
    return es_multiplo(numero,2)

#Ejercicio 2.7

def cantidad_de_pizzas(comensales:int, min_cant_de_porciones:int) -> int:
    pizza_entera = 8
    cant_pizzas = (comensales * min_cant_de_porciones) / pizza_entera

    return cant_pizzas

#EJERCICIO 3
#Ejercicio 3.1

def alguno_es_0(numero1:int,numero2:int) -> bool:

    return numero1 == 0 or numero2 == 0

#Ejercicio 3.2

def ambos_son_0(numero1:int,numero2:int) -> bool:

    return numero1 == 0 and numero2 == 0

#Ejercicio 3.3

def es_nombre_largo(nombre:str) -> bool:
    return len(nombre) >= 3 and len(nombre) <= 8

#Ejercicio 3.4

def es_bisiesto(anio:int) -> str:
    if es_multiplo(anio,400):
        print(f"{anio} es bisiesto")

    elif es_multiplo(anio,4) and not(es_multiplo(anio,100)):
        print(f"{anio} es bisiesto")
        
    else:
        print(f"{anio} no es bisiesto.")

print(es_bisiesto(2012))

#EJERCICIO 4
#Ejercicio 4.1

