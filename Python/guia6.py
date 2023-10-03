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
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero -1)

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

#print(es_bisiesto(2012))

#EJERCICIO 4
#Ejercicio 4.1

def peso_pino(altura:int) -> int:

    peso_total:int = 0
    altura_en_cm:int = altura * 100

    if altura <= 3:
        peso_total = altura_en_cm * 3
    else:
        primeros_3_metros = 3 * 100
        metros_restantes = altura_en_cm - primeros_3_metros
        peso_total = primeros_3_metros * 3 + metros_restantes * 2

    return peso_total 

def peso_util(peso:int) -> bool:
    return peso >=  400 and peso <= 1000

def sirve_pino(altura:int) -> bool:

    return peso_util(peso_pino(altura)) 

#EJERCICIO 5
#Ejercicio 5.1

def devolver_doble_si_par(numero:int) -> int:
    par = 2
    if numero % par == 0:
        resultado = numero * 2
    else:
        resultado = numero
    return resultado

#Ejercicio 5.2

def es_par(numero:int) -> int:
    return numero % 2 == 0

def devolver_valor_si_es_par_sino_el_que_sigue(numero:int) -> int:

    resultado:int = 0
    if es_par(numero):

        resultado = numero
    else:
        resultado = numero +1
    return resultado

#Ejercicio 5.3

def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero:int) -> int:
    resultado = 0

    if numero % 9 == 0:
        resultado = numero * 3
    elif numero % 3 == 0:
        resultado = numero * 2
    else:
        resultado = numero
    return resultado

#Ejercicio 5.4

def lindo_nombre(nombre:str) -> str:

    if len(nombre) >= 5:
        resultado:int = "Tu nombre tiene muchas letras"
    else:
        resultado:int = "Tu nombre tiene menos de 5 caracteres." 
    
    return resultado

#Ejercicio 5.5

def elRango(numero):

    if numero < 5:
        resultado:int = "Menor a 5"
    elif numero >= 10 and numero <= 20:
        resultado:int = "Entre 10 y 20"
    else:
        resultado:int = "Mayor a 20"
    
    return resultado

#Ejercicio 5.6

def vas_de_vacaciones(sexo: str, edad:int) -> str:
    
    if (sexo.lower() == "m" and edad >=  65) or (sexo.lower() == "f" and edad >=60):
        trabajo = "Anda de vacaciones"
    elif edad < 18:
        trabajo = "Anda de vacaciones"
    else:
        trabajo = "Te toca trabajar"
    
    return trabajo

#EJERCICIO 6

#Ejercicio 6.1

def numeros_1_a_10():
    numero = 1
    while numero <= 10:
        print(numero)
        numero += 1
    return

#Eejercicio 6.2

def pares_entre_numeros() -> int:
    numero = 10
    while numero <= 40:
        if numero % 2 == 0:
            print(numero)
        numero += 1
    return

#Ejercicio 6.3

def eco_10_veces():
    numero = 1
    while numero <= 10:
        print("ECO")
        numero += 1
    return

#Ejercicio 6.4

def cohete(numero:int):
    i = 0
    for i in range(i,numero,1):
    
        print(numero)
        numero -= 1
        if numero == 0:
            print("Despegue!!")

#Ejercicio 6.5

def viaje_en_el_tiempo_hacia_atras(anio_partida:int, anio_llegada:int) -> str:
    if anio_partida <= anio_llegada:
        print("El año de partida debe ser mayor que el año de llegada.")
        return
    
    while anio_llegada != anio_partida:
        print(f"“Viajo un anio al pasado, estamos en el anio: {anio_partida - 1}")
        anio_partida -= 1
    return
    
#Ejercicio 6.6

def viaje_aristoteles(anio_partida:int, anio_llegada:int) -> str:
    if anio_partida <= anio_llegada:
        print("El año de partida debe ser mayor que el año de llegada.")
        return
    
    while anio_partida >= -384:
        print(f"“Viajo un anio al pasado, estamos en el anio: {anio_partida - 20}")
        anio_partida -= 20

    return 

#Ejercicio 7 TODO


#EJERCICIO 8
#Ejercicio 8.1
def ejec_simbolica1():
    x = 5
    y = 7
    x = x+y
    print(x)

#Ejercicio 8.2
def ejec_simbolica2():
    x = 5
    y = 7
    z = x + y
    y = z * 2
    print(y)

#Ejercicio 8.3
def ejec_simbolica3():
    x = 5
    y = 7
    x = "hora"
    y = x *2
    print(y)

#Ejercicio 8.4

def ejec_simbolica4():
    x = False
    res = not(x)
    print(res)

#Ejercicio 8.5

def ejec_simbolica5():
    x = True
    y = False
    res = x and y
    x = res and x
    print(res) 
    print(x)
    
#EJERCICIO 9

def rt(x: int, g: int) -> int:
    g = g + 1
    return x + g

g: int = 0
def ro(x: int) -> int:
    global g
    g = g + 1
    return x + g

print(ro(1))
print(ro(1))
print(ro(1))

print(rt(1, 0))
print(rt(1, 0))
print(rt(1, 0))
