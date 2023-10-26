from queue import LifoQueue as Pila

def copiar(p: Pila) -> Pila:
    elementos: [int] = []
    while not p.empty():
        elementos.append(p.get())
    p_copy: Pila = Pila()
    
    for i in range(len(elementos)-1, 0-1,-1):
        
        p.put(elementos[i])
        p_copy.put(elementos[i])
    return p_copy

        
def buscar_maximo(pila):
    p_copy: Pila[int] = copiar(pila)
    value = pila.get()
    while not p_copy.empty():
       next_value =  p_copy.get()
       value = max(next_value, value)
    return value


pila = Pila()
pila.put(3)
pila.put(50)
pila.put(1)
pila.put(22)
pila.put(300)

#EJERCICIO 8
import random

def generar_nros_al_azar(cantidad:int, desde:int, hasta:int) -> Pila:
    pila = Pila()

    for _ in range(cantidad):

        numero_random = random.randint(desde, hasta)
        pila.put(numero_random)

    return pila

pila_num_random = generar_nros_al_azar(5,10,40)

while not pila_num_random.empty():
    print(pila_num_random.get()) 

