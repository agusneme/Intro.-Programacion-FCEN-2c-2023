import math
#Ejercicio 1
def hola_mundo():
    print("Hola mundo")
    
#hola_mundo()

#Ejercicio 2
def es_multiplo(n:int,m:int) -> bool:
    return  n %m == 0

#print(es_multiplo(10,2))   
#print(es_multiplo(3,7))     

#Ejercicio 3
def es_nombre_largo(nombre:str) -> bool:
    return len(nombre) >= 3 and len(nombre) <= 8

#Ejercicio 5
def devolver_doble_si_par(numero:int) -> int:
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

def pares_con_for() -> int:
    for num in range(10,41,2):
        print(num)
        
#print(pares_entre_numeros())
#pares_con_for()


#Ejercicio clase practica
def perimetro() -> float:
    res: float = 2*math.pi
    return res

#print(perimetro())

def cohete(numero:int):
    i = 0

    for i in range(i,numero,1):
        
        print(numero)
        numero -= 1

        if numero == 0:
            print("Despegue")
    

print(cohete(10))