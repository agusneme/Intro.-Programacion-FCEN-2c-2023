from queue import LifoQueue as Pila


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

#EJERCICIO 9

def cantidad_elementos(pila: Pila) -> int:
    # Crear una pila auxiliar para preservar los elementos
    pila_aux = Pila()
    # Contador de elementos
    contador = 0

    # Copiar elementos a la pila auxiliar y contar
    while not pila.empty():
        elemento = pila.get()
        pila_aux.put(elemento)
        contador += 1

    # Restaurar la pila original
    while not pila_aux.empty():
        elemento = pila_aux.get()
        pila.put(elemento)

    return contador

# Ejemplo de uso
pila = Pila()
pila.put(1)
pila.put(2)
pila.put(3)
pila.put(8)


cantidad = cantidad_elementos(pila)
print(f"La pila contiene {cantidad} elementos.")


#EJERCICIO 10
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

#EJERCICIO 11

def esta_bien_balanceada(s: str) -> bool:
    pila = Pila()  # Usamos LifoQueue como pila

    for caracter in s:
        if caracter == '(':
            pila.put(caracter)
        elif caracter == ')':
            if pila.empty():
                # Si encontramos un cierre de paréntesis sin una apertura correspondiente, la fórmula no está balanceada
                return False
            pila.get()  # Quitamos la apertura de paréntesis correspondiente

    # La fórmula está balanceada si la pila está vacía al final
    return pila.empty()

# Ejemplos de uso
formula_balanceada1 = "1 + (2 x 3 = (20 / 5))"
formula_balanceada2 = "10 * (1 + (2 * (1)))"
formula_no_balanceada = "1 + ) 2 x 3 ( ( )"

print(esta_bien_balanceada(formula_balanceada1))  # True
print(esta_bien_balanceada(formula_balanceada2))  # True
print(esta_bien_balanceada(formula_no_balanceada))  # False
