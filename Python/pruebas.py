from queue import Queue as Cola
import random

cola = Cola()
cola.put((1, "Paciente1", "Cardiología"))
cola.put((4, "Paciente2", "Dermatología"))
cola.put((2, "Paciente3", "Oftalmología"))
cola.put((6, "Paciente4", "Pediatría"))
cola.put((10, "Paciente5", "Neurología"))

def pacientes(c):
    prioridad = 0
    paciente_n = []
    while not c.empty():
        paciente = c.get()
        paciente_n.put(paciente)
    for tupla in paciente_n:
        if tupla[0] < 4:
            prioridad += 1
    return prioridad

print(pacientes(cola))