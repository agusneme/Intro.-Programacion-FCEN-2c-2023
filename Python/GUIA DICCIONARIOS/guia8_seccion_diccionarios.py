import csv


#EJERCICIO 19

def agrupar_por_longitud(archivo:str)  -> dict:

    diccionario_palabras :dict = {}

    with open(archivo, 'r') as texto:
        
        for linea in texto.readlines(): #Lee el archivo

            palabras = linea.split() #Divide cada linea en palabras
            for palabra in palabras:
                #Chequeo si diccionario esta cargado o no
                if len(palabra) in diccionario_palabras:
                    diccionario_palabras[len(palabra)] += 1
                else:
                    diccionario_palabras[len(palabra)] = 1

    texto.close()
    return diccionario_palabras

#print(agrupar_por_longitud('Intro.-Programacion-FCEN-2c-2023\Python\GUIA DICCIONARIOS\\texto.txt'))

#EJERCICIO 20

def promedio_estudiante(csv_notas) -> float:
    diccionario_notas:dict = {}

    with open(csv_notas, 'r', newline='') as notas:
        reader = csv.reader(notas)

        for columna in reader:

            lu = columna[0]
            nota = float(columna[3])
            
            if lu in diccionario_notas:
                diccionario_notas[lu]['notas'].append(nota)
            else:
                diccionario_notas[lu] = {'notas': [nota]}
    
    for lu, info in diccionario_notas.items():
        promedio = sum(info['notas']) / len(info['notas'])
        info['promedio'] = promedio

    return diccionario_notas




#EJERCICIO 21

def agrupar_por_palabras(archivo:str)  -> dict:
    diccionario_palabras :dict = {}

    with open(archivo, 'r') as texto:
        
        for linea in texto.readlines(): #Lee el archivo

            palabras = linea.split() #Divide cada linea en palabras
            for palabra in palabras:

                palabra = palabra.strip('.,!?()[]{"}:;').lower()

                #Chequeo si diccionario esta cargado o no
                if palabra in diccionario_palabras:
                    diccionario_palabras[palabra] += 1
                else:
                    diccionario_palabras[palabra] = 1

    texto.close()
    return diccionario_palabras

def la_palabra_mas_frecuente(archivo:str) -> str:

    diccionario = agrupar_por_palabras(archivo)
    palabara_mas_frecuente = max(diccionario, key=diccionario.get)

    return palabara_mas_frecuente
'''
print(agrupar_por_palabras('Intro.-Programacion-FCEN-2c-2023\Python\GUIA DICCIONARIOS\\texto.txt'))
print(la_palabra_mas_frecuente('Intro.-Programacion-FCEN-2c-2023\Python\GUIA DICCIONARIOS\\texto.txt'))
'''

