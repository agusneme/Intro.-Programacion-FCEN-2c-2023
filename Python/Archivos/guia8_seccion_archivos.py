#Revisar para optimizacion para ver si se puede sacar comentarios despues de un return

#Ejercicio 1
#1.1

def contar_lineas(archivo:str) -> int:
    contador = 0

    with open(archivo, "r") as archivo_open:
        for linea in archivo_open:
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
def cantidad_apariciones(archivo:str ,palabra:str)  -> int:
    return

#EJERCICIO 2
def es_comentario(linea:str) :    
    linea = linea.strip()
    return linea.startswith("#") 

def es_comentario_pruebas(linea) -> bool:
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
#------------------


#EJERCICIO 4

def agregar_frase_a_texto_final(archivo:str, frase:str) -> str:

    archivo_sin_frase = open(archivo, 'a')
    archivo_sin_frase.write('\n' + frase)

    archivo_sin_frase.close()

frase_final = 'Gracias. Buenas noches.'

#agregar_frase_a_texto_final('Intro.-Programacion-FCEN-2c-2023\Python\Archivos\\archivo_prueba.txt',frase)

#EJERCICIO 5

def agregar_frase_a_texto_comienzo(archivo:str, frase:str) -> str:
    with open(archivo, 'r') as file:
        contenido = file.read()

    with open(archivo, 'w') as file:
        file.write(frase + '\n')
        file.write(contenido)

#otra manera de hacerlo abriendolo en 'r+'

def agregar_frase_principio(archivo, frase):

    with open(archivo, 'r+') as archivo_original:
        contenido = archivo_original.read()
        archivo_original.seek(0)
        archivo_original.write(frase)
        archivo_original.write(contenido)
    

frase_inicio = 'Hola buenos dias.'

agregar_frase_a_texto_comienzo('Intro.-Programacion-FCEN-2c-2023\Python\Archivos\\archivo_prueba.txt',frase_inicio)

#EJERCICIO 6

def obtener_palabras_legibles(archivo) -> str:

    palabras_legibles = []
    palabra_actual = ''
    longitud_minima = 5

    with open(archivo, 'rb') as archivo_binario:
        contenido = archivo_binario.read().decode('utf-8')

        for caracter in contenido:

            if caracter.isalnum() or caracter in ' _':
                palabra_actual += caracter
            else:
                if len(palabra_actual) >= longitud_minima:
                    palabras_legibles.append(palabra_actual)
                palabra_actual = ''
        
        if len(palabra_actual) >= longitud_minima:
            palabras_legibles.append(palabra_actual)
    
    return palabras_legibles

#EJERCICIO 7

import csv

def promedio_estudiante(lu:str, csv_notas) -> float:

#nro de LU ( str ) , materia ( str ) , fecha ( str ) , nota ( float )

    with open(csv_notas, 'r', newline='') as notas:
        reader = csv.reader(notas)
        notas_estudiante = []

        for columna in reader:
            if columna[0] == lu:
                notas_estudiante.append(float(columna[3]))
        
        promedio = sum(notas_estudiante) / len(notas_estudiante)

    return promedio