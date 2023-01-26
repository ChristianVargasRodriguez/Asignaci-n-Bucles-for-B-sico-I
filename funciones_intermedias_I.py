# Actualizar valores en diccionarios y listas
# 1.- Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].
# 2.- Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
# 3.- En el directorio_deportes, cambia "Messi" por "Andrés".
# 4.- Cambia el valor 20 en z a 30.

x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#1
x[1][0] = 15 
print(x)
print("-"*30)
#2
estudiantes[0]['last_name'] = 'Bryant'
print(estudiantes)
print("-"*30)
#3
directorio_deportes['fútbol'][0] = "Andrés"
print(directorio_deportes)
#4
z[0]['y'] = 30
print(z)

print("-"*100)
# Iterar a través de una lista de diccionarios
# Crea una función iterateDictionary(some_list) para que, dada una lista de diccionarios, la función recorra cada diccionarios de la lista e imprima cada llave y el valor asociado. 
# Por ejemplo, dada la siguiente lista:

estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]


def iterateDictionary(some_list):
    for estud in some_list:
        estud_name = estud['first_name']
        estud_lastname = estud['last_name']
        llaves = []
        for llave in estudiantes[0]:
            llaves.append(llave)
        print(f" {llaves[0]} - {estud_name}, {llaves[1]} - {estud_lastname}")

iterateDictionary(estudiantes) 

# debería devolver: (está bien si cada par clave-valor termina en 2 líneas separadas;
# un bonus para que aparezcan exactamente como se muestra a continuación)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

print("-"*100)
# Obtener valores de una lista de diccionarios
# Crea una función iterateDictionary2(key_name, some_list) que, dada una lista de diccionarios y un nombre de clave, la función imprima el valor almacenado en esa clave para cada diccionario. Por ejemplo, iterateDictionary2('name', estudiantes) debería generar:


def iterateDictionary2(key_name, some_list):
    for i in some_list:
        for x in i:
            if key_name == x: 
                valor = i.get(key_name)
                print(valor)


iterateDictionary2('first_name', estudiantes)
print("-"*50)
iterateDictionary2('last_name', estudiantes)

print("-"*100)
# Iterar a través de un diccionarios con valores de lista
# Crea una función printInfo(some_dict) que, dado un diccionario cuyos valores son todos listas, imprima el nombre de cada clave junto con el tamaño de su lista, y luego imprima los valores asociados dentro de la lista de cada clave. Por ejemplo:

dojo = {
   'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(some_dict):
    someDict = some_dict
    for i in someDict:
        print(f"{len(someDict[i])} {i.upper()}")
        for x in someDict[i]:
            print(x)
        print("")

printInfo(dojo)

# # salida:
# 7 UBICACIONES
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORES
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon



# print("-"*50)
# def printInfo(some_dict):
#     some_dict = str(some_dict)
#     print(f"{len(dojo[some_dict])} {some_dict.upper()}")
#     for i in dojo[some_dict]:
#         print(i)
#     print("")
# printInfo('ubicaciones')
# printInfo('instructores')
