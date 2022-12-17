"""
Para ejecutar este archivo necesitas un archivo txt dentro de la misma carpeta que está este archivo y comentar el code que está antes de preferencia
Si no se especifica el metodo de entrada del archivo será por default r: (Read)
    Metodos:
        r: Read, lee si está el archivo si no existe manda error
        w: Write, si el archivo no existe lo crea, si existe lo sobreescribe
        a: Append, Añade el contenido al final del archivo ya existente
        r+: Lectura y escritura, La condición es que el archivo debe de existir
        rb: Lectura del archivo en bytes
        rb*: lo mismo que r+ pero en bytes
        wb: lo mismo que w pero en bytes
        w+: lo mismo que r+ pero si el archivo no existe, si existe lo sobreescribe

open("Ruta", "Método");
"""

#Opción 1
#Abrir el archivo rudimentariamente
from re import L


file= open('ejemplo.txt', 'r')
#print file
lineas=file.readlines()
print(lineas)
file.close

#Opcion 2
#abrir el archivo con un pseudónimo (cuando terminas de usarlo se cierra automáticamente)
with open('ejemplo2.txt','r') as archivo:
    lineas=archivo.readlines()
    print(lineas)

print(lineas) #esto o:
"""for l in lineas:
    print(l)"""
#si lo quieres sin espacios:
for l in lineas:
    print(l.replace('\n', ''))


#opcion 3
# pseudónimo con cambio (saca lista pero sin los \n)
with open('ejemplo3.txt', 'r') as archivo:
    contenido=archivo.read()
    lineas=contenido.split('\n')

#saber dónde estamos posicionados en un archivo
#regresa un numero que indica la posición del cursor (cuenta espacios y saltos de linea)
with open('ejemplo3.txt', 'r') as archivo:
    pos=archivo.tell()
    print (pos)
    #queremos saber cuantos caracteres tiene un archivo?
    print('el archivo tiene {0} caracteres de longitud'.format(pos))

#moverse a una posición específica dentro del archivo
with open('ejemplo3.txt', 'r') as archivo:
    archivo.seek(7)
    pos=archivo.tell()
    print(pos)
    contenido=archivo.read()
    lineas=contenido.split('\n')
    print(lineas)

#de el cursos moverse X elementos
with open('ejemplo3.txt', 'r') as archivo:
    siguientes=archivo.read(7)
    print(siguientes)

#________________________________________________________
#diferencias entre r y rb
#________________________________________________________

with open('ejemplo3.txt', 'r') as archivo:
    print(type(archivo.read()))#devuelve string

with open('ejemplo3.txt', 'rb') as archivo:
    print(type(archivo.read()))#devuelve byte

#método write (acuerdate que sobreescribe el documento)
with open('ejemplo4.txt', 'w') as archivo:
    archivo.write('Rodrigo\nBrenda\nRegina')

#método append (toma del ultimo punto y escribe después)
#es como si hicieras: 
# pos=archivo.tell()
# archivo.seek(pos)
with open('ejemplo3.txt', 'a') as archivo:
    archivo.write('Pedro\nLuis\nJorge')