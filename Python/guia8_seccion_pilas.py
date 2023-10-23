from queue import LifoQueue

def copiar(p: LifoQueue) -> LifoQueue:
    elementos: [int] = []
    while not p.empty():
        elementos.append(p.get())
    p_copy: LifoQueue = LifoQueue()
    
    for i in range(len(elementos)-1, 0-1,-1):
        
        p.put(elementos[i])
        p_copy.put(elementos[i])
    return p_copy

        
def buscar_maximo(pila):
    p_copy: LifoQueue[int] = copiar(pila)
    value = pila.get()
    while not p_copy.empty():
       next_value =  p_copy.get()
       value = max(next_value, value)
    return value


pila = LifoQueue()
pila.put(3)
pila.put(50)
pila.put(1)
pila.put(22)
pila.put(300)

print(pila.queue)
print(buscar_maximo(pila))