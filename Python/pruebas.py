def encontrar_ultima_posicion(lista, numero):
    for i in range(len(lista) - 1, -1, -1):
        if lista[i] == numero:
            return i
    return -1  # Retorna -1 si el número no se encuentra en la lista

# Ejemplo de uso:
mi_lista = [1, 2, 3, 4, 2, 5, 0]
numero_buscado = 2
ultima_posicion = encontrar_ultima_posicion(mi_lista, numero_buscado)

if ultima_posicion != -1:
    print(f"El número {numero_buscado} se encuentra en la última posición: {ultima_posicion}")
else:
    print(f"El número {numero_buscado} no se encuentra en la lista.")

