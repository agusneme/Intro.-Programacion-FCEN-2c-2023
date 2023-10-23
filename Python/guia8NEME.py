
#Revisar para optimizacion para ver si se puede sacar comentarios despues de un return
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
    

archivo_testeo = "texto_comentarios.py"
sacar_comentarios(archivo_testeo)


