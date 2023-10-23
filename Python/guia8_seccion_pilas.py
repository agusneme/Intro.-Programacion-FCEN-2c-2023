from queue import LifoQueue

def buscar_maximo(pila: LifoQueue[int]):
    
    maximo = 0
    for valor in pila.get():       
       if valor > maximo:
           maximo = valor
        
    return maximo 

pila = LifoQueue()
pila.put(3)
pila.put(50)
pila.put(1)
pila.put(22)
pila.put(300)


print(buscar_maximo(pila))