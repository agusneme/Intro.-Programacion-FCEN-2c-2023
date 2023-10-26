#Revisar para optimizacion para ver si se puede sacar comentarios despues de un return

#Ejercicio 1
#1.1

def contar_lineas(archivo:str) -> int:
    
    archivo_open = open(archivo, "r")
    contador = 0
    for linea in archivo_open.readlines():
        contador += 1
        
    archivo_open.close()
    
    return contador

#1.2

def existe_palabra(archivo:str, palabra:str) -> bool:
    
    archivo_open = open(archivo, "r")
    
    for linea in archivo_open.readlines():
        if palabra in linea.strip():
            return True
    return False

#1.3
def cantidad_apariciones(archivo:str ,palabra:str):
    return

#EJERCICIO 2
def es_comentario(linea:str):    
    linea = linea.strip()
    return linea.startswith("#") 

def es_comentario_pruebas(linea):
    for c in linea:
        if c != " ":
            if c == "#":
                return True
            return False
    return False

def sacar_comentarios(archivo:str):
    #Realizo apertura de archivos
    archivo_con_comentarios = open(archivo, "r")    
    archivo_sin_comentarios = open("clon_sin_comentarios.py", "w")
    
    #Recorrido de linea por linea y chequeo de existencia de comentarios
    for linea in archivo_con_comentarios.readlines():  
    
        if not es_comentario(linea):
            archivo_sin_comentarios.write(linea)
        
    #Cerrado de archivos
    archivo_con_comentarios.close()
    archivo_sin_comentarios.close()

#EJERCICIO 3

#EJERCICIO 4

def agregar_frase_a_texto(archivo:str, frase:str):

    archivo_sin_frase = open(archivo, 'a')
    archivo_sin_frase.write(frase)

    archivo_sin_frase.close()



frase = 'Hola buenos dias.'

agregar_frase_a_texto('Intro.-Programacion-FCEN-2c-2023\Python\Archivos\\archivo_prueba.txt',frase)