from queue import Queue as Cola
import random
#EJERCICIO 13
# Función para generar números al azar
def generar_nros_azar(n):
    cola = Cola()
    for _ in range(n):
        numero = random.randint(1, 100)  # Genera números aleatorios entre 1 y 100
        cola.put(numero)  # Agrega el número a la cola
    return cola

# Ejemplo de uso
n = 4  # Cantidad de números al azar a generar
cola_de_numeros = generar_nros_azar(n)

# Imprimir la cola de números generados
while not cola_de_numeros.empty():
    numero = cola_de_numeros.get()
    print(numero)

#EJERCICIO 14
def cantidad_elementos(cola: Cola) -> int:
    # Contador de elementos
    contador = 0

    # Consumir elementos y contar
    while not cola.empty():
        elemento = cola.get()
        contador += 1

    return contador

# Ejemplo de uso
cola = Cola()
cola.put(1)
cola.put(2)
cola.put(3)

cantidad = cantidad_elementos(cola)
print(f"La cola contiene {cantidad} elementos.")

from queue import Queue

def buscar_maximo(cola: Queue) -> int:
    if cola.empty():
        raise ValueError("La cola está vacía, no se puede buscar un máximo.")

    maximo = cola.queue[0]  # Suponemos que el primer elemento es el máximo inicial

    # Recorremos la cola para encontrar el máximo
    for elemento in cola.queue:
        if elemento > maximo:
            maximo = elemento

    return maximo

# Ejemplo de uso
cola = Queue()
cola.put(5)
cola.put(10)
cola.put(252)
cola.put(8)

maximo = buscar_maximo(cola)
print(f"El elemento máximo en la cola es: {maximo}")

#EJERCICIO 17

# Definimos la cola con elementos de la forma (prioridad, nombre, especialidad)
cola = Cola()
cola.put((1, "Paciente1", "Cardiología"))
cola.put((4, "Paciente2", "Dermatología"))
cola.put((2, "Paciente3", "Oftalmología"))
cola.put((6, "Paciente4", "Pediatría"))
cola.put((10, "Paciente5", "Neurología"))

def n_pacientes_urgentes(cola):
    contador = 0

    # Recorremos la cola y contamos los pacientes con prioridad en el rango [1, 3]
    for elemento in cola.queue:
        prioridad, _, _ = elemento
        if 1 <= prioridad <= 3:
            contador += 1

    return contador

cantidad_urgentes = n_pacientes_urgentes(cola)
print(f"La cantidad de pacientes urgentes es: {cantidad_urgentes}")
