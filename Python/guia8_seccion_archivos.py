#Ejercicio 1
#1.1

def contar_lineas(archivo:str) -> int:
    
    archivo_open = open(archivo, "r")
    contador = 0
    for linea in archivo_open.readlines():
        contador += 1
        
    archivo_open.close()
    
    return contador

print(contar_lineas("texto_pruebas.txt"))

#1.2

def existe_palabra(archivo:str, palabra:str) -> bool:
    
    archivo_open = open(archivo, "r")
    
    for linea in archivo_open.readlines():
        if palabra in linea.strip():
            return True
    return False

print(existe_palabra("texto_pruebas.txt", "perro"))

#1.3
def cantidad_apariciones(archivo:str ,palabra:str):
    
    

print(cantidad_apariciones("texto_pruebas.txt", "hola"))